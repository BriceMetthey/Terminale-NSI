def recherche_naive(tab: list, x: int) -> int:
    """
    Recherche l'élément x dans le tableau tab
    Renvoie l'indice de l'élément x trouvé
    Sinon renvoie -1
    """
    for i in range(len(tab)):
        if tab[i] == x:
            return i

    return -1


# Tests unitaires
tableau = [2, 3, 4, 5, 6, 7, 8, 9]
assert recherche_naive(tableau, 9) == 7
assert recherche_naive(tableau, 4) == 2
assert recherche_naive(tableau, 10) == -1
