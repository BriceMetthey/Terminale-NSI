def fusion(T1: list, T2: list) -> list:
    """
    Fusionne les deux tableaux triés T1 et T2
    """

    T = [0] * (len(T1) + len(T2))
    i1 = i2 = j = 0  # indices des piles

    # Tant que les deux piles sont non vides
    while i1 < len(T1) and i2 < len(T2):
        if T1[i1] < T2[i2]:
            T[j] = T1[i1]
            i1 += 1
        else:
            T[j] = T2[i2]
            i2 += 1
        j += 1

    # Une des deux piles est vide :
    # seule une des 2 boucles while est exécutée!
    while i1 < len(T1):
        T[j] = T1[i1]
        i1 += 1
        j += 1

    while i2 < len(T2):
        T[j] = T2[i2]
        i2 += 1
        j += 1

    return T


def tri_fusion(T: list) -> list:
    """
    Renvoie un tableau T trié
    """

    n = len(T)
    # Cas de base
    if n < 2:
        return T[:]  # copie de T

    # Diviser : découpe de T
    T1 = T[0 : n // 2]
    T2 = T[n // 2 : n]

    # Résoudre : appels récursifs
    T1 = tri_fusion(T1)
    T2 = tri_fusion(T2)

    # Combiner : fusion des tableaux triés
    return fusion(T1, T2)


# Tests unitaires
tab_a_trier = [7, 5, 3, 0, 1, 6, 4, 2]
assert tri_fusion(tab_a_trier) == [0, 1, 2, 3, 4, 5, 6, 7]
