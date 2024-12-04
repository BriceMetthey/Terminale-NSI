def recherche(lst: list, x: int):
    """
    Recherche un élément x dans un tableau lst (approche dichotomique récursive).
    """

    if len(lst) == 0:
        return False

    m = len(lst) // 2

    if lst[m] == x:
        return True

    elif lst[m] < x:
        return recherche(lst[m + 1 :], x)  # on va chercher sur la partie droite

    else:
        return recherche(lst[:m], x)  # on va chercher sur la partie gauche


# Tests unitaires
tableau = [4, 5, 7, 8, 9, 14, 46, 89]
assert recherche(tableau, 46) == True
assert recherche(tableau, 2) == False
