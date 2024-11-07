# Fonction pour créer une liste vide
def creer_liste():
    return ()

# Fonction pour vérifier si la liste est vide
def est_vide(liste):
    return liste == ()

# Fonction pour ajouter un élément en tête
def ajouter_en_tete(liste, element):
    return (element, liste)

# Fonction pour ajouter un élément en queue
def ajouter_en_queue(liste, valeur):
    if est_vide(liste):
        return (valeur, ())
    else:
        head, next_node = liste
        return (head, ajouter_en_queue(next_node, valeur))

# Fonction pour ajouter un élément à une position spécifique
def ajouter(liste, valeur, position):
    if position == 0 or est_vide(liste):
        return ajouter_en_tete(liste, valeur)
    else:
        head, next_node = liste
        return (head, ajouter(next_node, valeur, position - 1))

# Fonction pour supprimer l'élément en tête
def supprimer_en_tete(liste):
    if est_vide(liste):
        return ()
    _, next_node = liste
    return next_node

# Fonction pour supprimer l'élément en queue
def supprimer_en_queue(liste):
    if est_vide(liste) or liste[1] == ():
        return ()
    head, next_node = liste
    if next_node[1] == ():
        return (head, ())
    return (head, supprimer_en_queue(next_node))

# Fonction pour supprimer un élément à une position spécifique
def supprimer(liste, position):
    if est_vide(liste):
        return ()
    if position == 0:
        return supprimer_en_tete(liste)
    head, next_node = liste
    return (head, supprimer(next_node, position - 1))

# Fonction pour chercher une valeur dans la liste
def chercher(liste, valeur):
    if est_vide(liste):
        return False
    head, next_node = liste
    if head == valeur:
        return True
    return chercher(next_node, valeur)

# Fonction pour accéder au nième élément
def nieme_element(liste, position):
    if est_vide(liste):
        raise IndexError("Position hors de la liste")
    if position == 0:
        return liste[0]
    _, next_node = liste
    return nieme_element(next_node, position - 1)

# Fonction pour parcourir la liste et afficher les valeurs
def parcourir(liste):
    if est_vide(liste):
        print('None')
        return
    head, next_node = liste
    print(head, end=' -> ')
    parcourir(next_node)

# Fonction pour calculer la taille de la liste
def taille(liste):
    if est_vide(liste):
        return 0
    _, next_node = liste
    return 1 + taille(next_node)

# Fonction pour renverser la liste chaînée
def renverser(liste):
    acc = ()
    while not est_vide(liste):
        head, next_node = liste
        acc = (head, acc)
        liste = next_node
    return acc


# Exemple d'utilisation
liste = creer_liste()  # Liste vide
liste = ajouter_en_tete(liste, 1)
liste = ajouter_en_tete(liste, 2)
liste = ajouter_en_tete(liste, 3)
liste = ajouter_en_queue(liste, 4)
liste = ajouter(liste, 5, 2)

parcourir(liste)  # Affiche la liste
print("Taille de la liste:", taille(liste))

liste = supprimer_en_tete(liste)
liste = supprimer_en_queue(liste)
parcourir(liste)  # Affiche la liste après suppressions

print("Recherche 3 dans la liste:", chercher(liste, 3))
print("Recherche 6 dans la liste:", chercher(liste, 6))

print("Élément à la position 1:", nieme_element(liste, 1))

liste = renverser(liste)
parcourir(liste)  # Affiche la liste inversée
