def element_majoritaire(tab: list, debut: int, fin: int):
    """
    Renvoi l'élément majoritaire du tableau tab qui apparaît plus de n//2 fois.
    """

    # Si le tableau contient un seul élément
    if debut == fin:
        return tab[debut]

    # Diviser le tableau en deux moitiés
    milieu = (debut + fin) // 2

    # Trouver les éléments majoritaires dans chaque sous-tableau
    maj_gauche = element_majoritaire(tab, debut, milieu)
    maj_droite = element_majoritaire(tab, milieu + 1, fin)

    # Si les deux moitiés ont le même majoritaire
    if maj_gauche == maj_droite:
        return maj_gauche

    # Compter les occurrences des deux candidats
    count_gauche = 0
    count_droite = 0
    for i in range(debut, fin + 1):
        if tab[i] == maj_gauche:
            count_gauche += 1
        if tab[i] == maj_droite:
            count_droite += 1

    # Vérifier lequel est majoritaire
    taille = fin - debut + 1
    if count_gauche > taille // 2:
        return maj_gauche
    if count_droite > taille // 2:
        return maj_droite

    return None  # Aucun élément majoritaire


# Tests unitaires
tableau = [3, 3, 4, 2, 4, 4, 2, 4, 4]
assert element_majoritaire(tableau, 0, len(tableau) - 1) == 4

tableau = [3, 3, 4, 5, 4, 6, 2, 4, 4, 10]
assert element_majoritaire(tableau, 0, len(tableau) - 1) == None
