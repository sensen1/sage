from sage.categories.commutative_additive_groups import CommutativeAdditiveGroups
from sage.categories.groups import Groups
from sage.structure.element import MultiplicativeGroupElement
from sage.structure.unique_representation import UniqueRepresentation
from sage.structure.parent import Parent
from sage.sets.cartesian_product import CartesianProduct
from sage.misc.cachefunc import cached_method
from sage.groups.group_exp import GroupExp

class GroupSemidirectProductElement(CartesianProduct.Element):
    r"""
    Element class for :class:`GroupSemidirectProduct`.
    """

    def _repr_(self):

        def wrapper(prefix, s):
            if prefix is None:
                return s
            return "%s[%s]"%(prefix,s)

        par = self.parent()

        g = self.summand_projection(0)
        h = self.summand_projection(1)
        gstr = wrapper(par._prefix0, g.__repr__())
        hstr = wrapper(par._prefix1, h.__repr__())
        if par._print_tuple:
            return "(%s, %s)"%(gstr,hstr)

        if self == par.one():
            return "1"
        if g == g.parent().one():
            return hstr
        if h == h.parent().one():
            return gstr
        return gstr + " * " + hstr

    def inverse(self):
        par = self.parent()
        g = self.summand_projection(0)
        h = self.summand_projection(1)

        if par.act_to_right():
            return self.__class__(par,(~g, par._twist(g,~h)))
        else:
            hi = ~h
            return self.__class__(par,(par._twist(hi,~g),hi))

    __invert__ = inverse

    def to_opposite(self):
        r"""
        Send an element to its image in the opposite semidirect product.

        EXAMPLES::

            sage: L = RootSystem(['A',2]).root_lattice(); L
            Root lattice of the Root system of type ['A', 2]
            sage: from sage.groups.group_exp import GroupExp
            sage: EL = GroupExp()(L)
            sage: W = L.weyl_group(prefix="s"); W
            Weyl Group of type ['A', 2] (as a matrix group acting on the root lattice)
            sage: def twist(w,v):
            ...       return EL(w.action(v.value))
            sage: G = GroupSemidirectProduct(W, EL, twist, prefix1='t'); G
            Semidirect product of Weyl Group of type ['A', 2] (as a matrix group acting on the root lattice) acting on Multiplicative form of Root lattice of the Root system of type ['A', 2]
            sage: mu = L.an_element(); mu
            2*alpha[1] + 2*alpha[2]
            sage: w = W.an_element(); w
            s1*s2
            sage: g = G((w,EL(mu))); g
            s1*s2 * t[2*alpha[1] + 2*alpha[2]]
            sage: g.to_opposite()
            t[-2*alpha[1]] * s1*s2
            sage: g.to_opposite().parent()
            Semidirect product of Multiplicative form of Root lattice of the Root system of type ['A', 2] acted upon by Weyl Group of type ['A', 2] (as a matrix group acting on the root lattice)

        """
        par = self.parent()
        Gop = par.opposite_semidirect_product()
        g = self.summand_projection(0)
        h = self.summand_projection(1)
        if par.act_to_right():
            return Gop((par._twist(g,h),g))
        return Gop((h,par._twist(~h,g)))

class GroupSemidirectProduct(CartesianProduct):

    r"""
    Returns the semidirect product of the groups ``G`` and ``H`` using the homomorphism ``twist``.

    INPUT:

        - ``G`` and ``H`` -- multiplicative groups
        - ``twist`` -- (default: None) a group homomorphism (see below)
        - ``act_to_right`` -- True or False (default: True)
        - ``prefix0`` -- (default: None) optional string
        - ``prefix1`` -- (default: None) optional string
        - ``print_tuple`` -- True or False (default: False)
        - ``category`` -- A category (default: Groups())

    If ``act_to_right`` is True, ``twist`` is an element of ``Hom(G, Aut(H))``. Syntactically
    ``twist(g,h)`` is in ``H`` for all `g\in G` and `h\in H`.
    If ``act_to_right`` is False, ``twist`` is an element of ``Hom(H, Aut(G))``
    and ``twist(h,g)`` is in ``G`` for all `g\in G` and `h\in H`.
    If ``prefix0`` (resp. ``prefixl``) is not None then it is used as a wrapper for
    printing elements of ``G`` (resp. ``H``). If ``print_tuple`` is True then elements are printed
    in the style `(g,h)` and otherwise in the style `g * h`.


    EXAMPLES::

        sage: G = GL(2,QQ)
        sage: V = QQ^2
        sage: EV = GroupExp()(V) # make a multiplicative version of V
        sage: def twist(g,v):
        ...       return EV(g*v.value)
        sage: H = GroupSemidirectProduct(G, EV, twist=twist, prefix1 = 't'); H
        Semidirect product of General Linear Group of degree 2 over Rational Field acting on Multiplicative form of Vector space of dimension 2 over Rational Field
        sage: x = H.an_element(); x
        t[(1, 0)]
        sage: x^2
        t[(2, 0)]
        sage: cartan_type = CartanType(['A',2])
        sage: W = WeylGroup(cartan_type, prefix="s")
        sage: def twist(w,v):
        ...       return w*v*(~w)
        sage: WW = GroupSemidirectProduct(W,W, twist=twist, print_tuple=True)
        sage: s = Family(cartan_type.index_set(), lambda i: W.simple_reflection(i))
        sage: y = WW((s[1],s[2])); y
        (s1, s2)
        sage: y^2
        (1, s2*s1)
        sage: y.inverse()
        (s1, s1*s2*s1)

    TODO: Functorial constructor for semidirect products for various categories
    Twofold Direct product as a special case of semidirect product

    """

    def __init__(self, G, H, twist=None, act_to_right=True, prefix0=None, prefix1=None, print_tuple=False,category=Groups()):
        self._act_to_right = act_to_right
        def check_implemented_group(x):
            if x in Groups():
                return
            error = "The semidirect product construction for groups is implemented only for multiplicative groups"
            if x in CommutativeAdditiveGroups():
                error = error + ". Please change the commutative additive group %s into a multiplicative group using the functor sage.groups.group_exp.GroupExp"%x
            raise TypeError, error

        check_implemented_group(G)
        check_implemented_group(H)

        if twist is None:
            self._twist = lambda g,h: h # use the trivial twist
        else:
            self._twist = twist

        self._prefix0 = prefix0
        self._prefix1 = prefix1
        self._print_tuple = print_tuple
        self._category = category
        CartesianProduct.__init__(self, (G,H), category=category)

    def act_to_right(self):
        return self._act_to_right

    def _repr_(self):
        summands = self.summands()
        if self.act_to_right():
            act_string = "acting on"
        else:
            act_string = "acted upon by"
        return "Semidirect product of %s %s %s"%(summands[0],act_string, summands[1])

    def _element_constructor_(self, x):
        def type_error():
            raise TypeError, "%s cannot be converted into an element of %s"%(x,self)

        if isinstance(x, self.element_class) and x.parent() == self:
            return x
        if not isinstance(x, GroupSemidirectProductElement):
            if not isinstance(x, tuple):
                type_error()
            if len(x) != 2:
                type_error()
            g, h = x
        else:
            g = x.summand_projection(0)
            h = x.summand_projection(1)
        gg = self.summands()[0](g)
        hh = self.summands()[1](h)
        return self._cartesian_product_of_elements((gg,hh))

    @cached_method
    def one(self):
        return self((self.summands()[0].one(), self.summands()[1].one()))

    def product(self, x, y):
        xg = x.summand_projection(0)
        xh = x.summand_projection(1)
        yg = y.summand_projection(0)
        yh = y.summand_projection(1)
        if self.act_to_right():
            g = xg * yg
            h = self._twist(~yg,xh) * yh
        else:
            h = xh * yh
            g = xg * self._twist(xh,yg)
        return self((g,h))

    @cached_method
    def opposite_semidirect_product(self):
        r"""
        Create the same semidirect product but with the positions of the groups exchanged.

        EXAMPLES::

            sage: G = GL(2,QQ)
            sage: L = QQ^2
            sage: EL = GroupExp()(L)
            sage: H = GroupSemidirectProduct(G, EL, twist = lambda g,v: EL(g*v.value), prefix1 = 't'); H
            Semidirect product of General Linear Group of degree 2 over Rational Field acting on Multiplicative form of Vector space of dimension 2 over Rational Field
            sage: h = H((Matrix([[0,1],[1,0]]), EL.an_element())); h
            [0 1]
            [1 0] * t[(1, 0)]
            sage: Hop = H.opposite_semidirect_product(); Hop
            Semidirect product of Multiplicative form of Vector space of dimension 2 over Rational Field acted upon by General Linear Group of degree 2 over Rational Field
            sage: hop = h.to_opposite(); hop
            t[(0, 1)] * [0 1]
            [1 0]
            sage: hop in Hop
            True

        """

        return GroupSemidirectProduct(self.summands()[1], self.summands()[0], twist=self._twist, act_to_right = not self.act_to_right(), prefix0 = self._prefix1, prefix1 = self._prefix0, print_tuple = self._print_tuple, category=self._category)

GroupSemidirectProduct.Element = GroupSemidirectProductElement

