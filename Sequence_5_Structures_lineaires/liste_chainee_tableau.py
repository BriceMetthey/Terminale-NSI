# Fonction pour créer une liste vide
def creer_liste():
    return []  # Une liste vide est représentée par une liste Python vide

# Fonction pour vérifier si la liste est vide
def est_vide(liste):
    return len(liste) == 0

# Fonction pour ajouter un élément en tête
def ajouter_en_tete(liste, valeur):
    return [valeur] + liste

# Fonction pour ajouter un élément en queue
def ajouter_en_queue(liste, valeur):
    return liste + [valeur]

# Fonction pour ajouter un élément à une position spécifique
def ajouter(liste, valeur, position):
    assert position >= 0
    if position == 0:
        return ajouter_en_tete(liste, valeur)
    elif position >= len(liste):
        return ajouter_en_queue(liste, valeur)
    else:
        return liste[:position] + [valeur] + liste[position:]

# Fonction pour supprimer l'élément en tête
def supprimer_en_tete(liste):
    if est_vide(liste):
        return []
    return liste[1:]

# Fonction pour supprimer l'élément en queue
def supprimer_en_queue(liste):
    if est_vide(liste):
        return []
    return liste[:-1]

# Fonction pour supprimer un élément à une position spécifique
def supprimer(liste, position):
    if est_vide(liste) or position < 0 or position >= len(liste):
        return liste  # Retourne la liste inchangée si la position est invalide
    return liste[:position] + liste[position + 1:]

# Fonction pour chercher une valeur dans la liste
def chercher(liste, valeur):
    return valeur in liste

# Fonction pour accéder au nième élément
def nieme_element(liste, position):
    if position < 0 or position >= len(liste):
        raise IndexError("Position hors de la liste")
    return liste[position]

# Fonction pour parcourir la liste et afficher les valeurs
def parcourir(liste):
    for elem in liste:
        print(elem, end=' -> ')
    print('None')

# Fonction pour calculer la taille de la liste
def taille(liste):
    return len(liste)

# Fonction pour renverser la liste chaînée
def renverser(liste):
    return liste[::-1]

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
