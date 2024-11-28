def recherche_dichotomique(tab, val):
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
        else: # on a tab[milieu] < val
            # on cherche entre milieu + 1 et droite
            gauche = milieu + 1
   
    # on est sorti de la boucle sans trouver val
    return -1