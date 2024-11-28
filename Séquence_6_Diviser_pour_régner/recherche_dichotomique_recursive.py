def recherche(lst, x):
    
    if len(lst) == 0:
        return False
    
    m = len(lst) // 2
    
    if lst[m] == x:
        return True
    
    elif lst[m] < x :
        return recherche(lst[m + 1 :], x) # on va chercher sur la partie droite
    
    else :
        return recherche(lst[:m], x) # on va chercher sur la partie gauche