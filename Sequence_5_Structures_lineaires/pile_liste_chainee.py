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
    


if __name__ == "__main__":
    
    # Création de la pile
    pile = Pile()

    # Empiler des éléments
    pile.empiler(10)
    pile.empiler(20)
    pile.empiler(30)

    # Afficher le sommet actuel
    print("Sommet:", pile.sommet_valeur())  # Affiche 30

    # Dépiler les éléments
    print("Dépile:", pile.depiler())  # Affiche 30
    print("Dépile:", pile.depiler())  # Affiche 20

    # Vérifier si la pile est vide
    print("La pile est vide :", pile.est_vide())  # Affiche False

    # Dernier dépilement
    print("Dépile:", pile.depiler())  # Affiche 10
    print("La pile est vide :", pile.est_vide())  # Affiche True
