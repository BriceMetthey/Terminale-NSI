def recherche_max(tab: list, debut: int, fin: int) -> int:
    """
    Trouver le plus grand élément dans un tableau tab de n éléments en utilisant une approche "diviser pour régner".
    """

    # Si le tableau contient un seul élément
    if debut == fin:
        return tab[debut]

    # Diviser le tableau en deux moitiés
    milieu = (debut + fin) // 2

    # Trouver le maximum dans chaque moitié
    max_gauche = recherche_max(tab, debut, milieu)
    max_droite = recherche_max(tab, milieu + 1, fin)

    # Combiner les résultats
    return max(max_gauche, max_droite)


# Test unitaire
tab = [3, 1, 4, 1, 5, 9, 2, 6]
assert recherche_max(tab, 0, len(tab) - 1) == 9
