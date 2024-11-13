def creer_pile(n):
    """
    Une pile vide est un tuple formé
    d'un tableau de n éléments et d'une taille de 0
    """
    return ([None] * n, 0)

def pile_vide(pile):
    _, top = pile
    return top == 0

def pile_pleine(pile):
    t, top = pile
    return top == len(t)

def empiler(pile, element):
    assert not pile_pleine(pile)
    t, top = pile
    t[top] = element
    return (t, top + 1)

def depiler(pile):
    assert not pile_vide(pile)
    t, top = pile
    return (t, top-1)

def sommet(pile):
    assert not pile_vide(pile)
    t, top = pile
    return t[top-1]

def elements_pile(pile):
    res = []
    t, top = pile
    for i in range(top, 0, -1):
        res.append(t[i-1])
    return res


pile = creer_pile(10)
pile = empiler(pile, "Alice")
pile = empiler(pile, "Bob")
pile = empiler(pile, "Charlie")

assert sommet(pile) == "Charlie"
pile = depiler(pile)
assert pile_vide(pile) == False

for e in elements_pile(pile):
    print(e)

pile = depiler(pile)
pile = depiler(pile)
assert pile_vide(pile) == True