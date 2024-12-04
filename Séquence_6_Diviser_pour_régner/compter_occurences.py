def compter_occurrences(tab: list, debut: int, fin: int, x: int):
    """
    Permet de compter le nombre de fois qu'un élément x apparaît dans le tableau tab.
    """

    # Cas de base : un seul élément
    if debut == fin:
        if tab[debut] == x:
            return 1
        else:
            return 0

    # Diviser le tab en deux moitiés
    milieu = (debut + fin) // 2
    gauche = compter_occurrences(tab, debut, milieu, x)
    droite = compter_occurrences(tab, milieu + 1, fin, x)

    # Combiner les résultats
    return gauche + droite


# Tests unitaires
tableau = [1, 3, 2, 3, 3, 4, 3, 5]
assert compter_occurrences(tableau, 0, len(tableau) - 1, 3) == 4
assert compter_occurrences(tableau, 0, len(tableau) - 1, 5) == 1
assert compter_occurrences(tableau, 0, len(tableau) - 1, 25) == 0
