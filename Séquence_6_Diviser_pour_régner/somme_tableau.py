def somme_tab(tab: list, debut: int, fin: int) -> int:
    """
    Calculer la somme de tous les éléments d'un tableau tab de n éléments en utilisant l'approche "diviser pour régner"

    Parameters:
    tab (list): Tableau tab de n éléments
    debut (int): Indice de départ du tableau à calculer
    fin (int): Indice de fin du tableau à calculer
    Returns:
    int: La somme de tous les éléments du tableau tab
    """

    # Si le tableau contient un seul élément
    if debut == fin:
        return tab[debut]

    # Diviser le tableau en deux moitiés
    milieu = (debut + fin) // 2

    # Somme récursive pour chaque moitié
    somme_gauche = somme_tab(tab, debut, milieu)
    somme_droite = somme_tab(tab, milieu + 1, fin)

    # Combiner les résultats
    return somme_gauche + somme_droite


# Tests unitaires
tab = [3, 1, 4, 1, 5, 9, 2, 6]
assert somme_tab(tab, 0, len(tab) - 1) == 31
