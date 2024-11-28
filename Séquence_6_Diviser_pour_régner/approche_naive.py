def recherche_naive(tab, val):

    for i in range(len(tab)):
        if tab[i] == val:
            return i
    
    return -1