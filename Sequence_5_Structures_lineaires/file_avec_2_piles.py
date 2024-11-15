class Cellule:
    def __init__(self, v, s):
        self.valeur = v  
        self.suivante = s  

class Pile:
    def __init__(self):
        self.sommet = None  # Le sommet de la pile, initialement vide

    def est_vide(self):
        """Vérifie si la pile est vide."""
        return self.sommet is None

    def empiler(self, valeur):
        """Empile un élément au sommet de la pile."""
        nouvelle_cellule = Cellule(valeur, None)  # Crée une nouvelle Cellule
        nouvelle_cellule.suivante = self.sommet  # Le pointeur de la nouvelle cellule pointe vers l'ancien sommet
        self.sommet = nouvelle_cellule  # La nouvelle cellule devient le sommet

    def depiler(self):
        """Dépile l'élément au sommet de la pile et le retourne."""
        if self.est_vide():
            raise IndexError("depiler depuis une pile vide")  # Erreur si la pile est vide
        valeur = self.sommet.valeur  # Sauvegarde la valeur du sommet
        self.sommet = self.sommet.suivante  # Le sommet devient la cellule suivante
        return valeur  # Retourne la valeur dépilée

    def sommet_valeur(self):
        """Retourne la valeur au sommet sans dépiler."""
        if self.est_vide():
            raise IndexError("sommet_valeur depuis une pile vide")
        return self.sommet.valeur


class File:

    """structure de file en utilant 2 piles"""
    def __init__(self):
        self.entree = Pile()
        self.sortie = Pile()

    def est_vide(self):
        return self.entree.est_vide()  and self.sortie.est_vide()

    def enfiler(self, x):
        self.entree.empiler(x)

    def defiler(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empiler(self.entree.depiler())
        if self.sortie.est_vide():
            raise IndexError("retirer sur une file vide")
        return self.sortie.depiler()



f = File()
f.enfiler(1)
f.enfiler(2)
f.enfiler(3)
f.enfiler(4)
assert f.defiler() == 1
assert f.defiler() == 2
assert f.defiler() == 3