from Cellule import Cellule
from liste_poo_rec import *

class ListeChainee:
    def __init__(self):
        self.tete = None

    def est_vide(self):
        return self.tete is None

    def ajouter_en_tete(self, valeur):
        self.tete = Cellule(valeur, self.tete)

    def ajouter_en_queue(self, valeur):
        if self.est_vide():
            self.tete = Cellule(valeur, None)
        else:
            ajouter_en_queue_rec(self.tete, valeur)



    def ajouter(self, valeur, position):
        if position <= 0 or self.est_vide():
            self.ajouter_en_tete(valeur)
        else:
            ajouter_rec(self.tete, valeur, position)



    def supprimer_en_tete(self):
        if not self.est_vide():
            self.tete = self.tete.suivante

    def supprimer_en_queue(self):
        if self.est_vide():
            return
        if self.tete.suivante is None:
            self.tete = None
        else:
            supprimer_en_queue_rec(self.tete)



    def supprimer(self, position):
        if position == 0:
            self.supprimer_en_tete()
        elif not self.est_vide():
            supprimer_rec(self.tete, position)



    def chercher(self, valeur):
        return chercher_rec(self.tete, valeur)



    def nieme_element(self, position):
        return nieme_rec(self.tete, position)



    def parcourir(self):
        parcourir_rec(self.tete)



    def taille(self):
        return taille_rec(self.tete)



    def renverser(self):
        self.tete = renverser_rec(self.tete)



# Exemple d'utilisation
liste = ListeChainee()
liste.ajouter_en_tete(1)
liste.ajouter_en_tete(2)
liste.ajouter_en_tete(3)
liste.ajouter_en_queue(4)
liste.ajouter(5, 2)

liste.parcourir()  # Affiche la liste
print("Taille de la liste:", liste.taille())

liste.supprimer_en_tete()
liste.supprimer_en_queue()
liste.parcourir()  # Affiche la liste après suppressions

print("Recherche 3 dans la liste:", liste.chercher(3))
print("Recherche 6 dans la liste:", liste.chercher(6))

print("Élément à la position 1:", liste.nieme_element(1))

liste.renverser()
liste.parcourir()  # Affiche la liste inversée
