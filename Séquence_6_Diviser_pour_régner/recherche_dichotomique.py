def recherche_dichotomique(tab: list, val: int) -> int:
    """
    Recherche un élément val dans un tableau trié tab (approche dichotomique itérative).
    Renvoie la position de l'élément cherché si il est trouvé.
    Sinon renvoie -1.
    """
    gauche = 0
    droite = len(tab) - 1

    while gauche <= droite:

        milieu = (gauche + droite) // 2
        if tab[milieu] == val:
            # on a trouvé val dans le tableau,
            # à la position milieu
            return milieu

        elif tab[milieu] > val:
            # on cherche entre gauche et milieu - 1
            droite = milieu - 1
        else:  # on a tab[milieu] < val
            # on cherche entre milieu + 1 et droite
            gauche = milieu + 1

    # on est sorti de la boucle sans trouver val
    return -1


# Tests unitaires
tableau = [1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 33, 45, 67]
assert recherche_dichotomique(tableau, 33) == 10
assert recherche_dichotomique(tableau, 2) == 1
assert recherche_dichotomique(tableau, 55) == -1
