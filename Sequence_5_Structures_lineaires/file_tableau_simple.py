class FileTableauSimple:
    def __init__(self, capacite):
        self.capacite = capacite                # Capacité maximale de la file
        self.tableau = [None] * capacite        # Tableau de taille fixe
        self.taille = 0                         # Nombre d'éléments dans la file

    def est_vide(self):
        return self.taille == 0

    def est_pleine(self):
        return self.taille == self.capacite

    def enfiler(self, valeur):
        if self.est_pleine():
            raise OverflowError("La file est pleine")
        
        # Ajouter l'élément à la fin de la file
        self.tableau[self.taille] = valeur
        self.taille += 1

    def defiler(self):
        if self.est_vide():
            raise IndexError("La file est vide")
        
        # Récupérer l'élément au début de la file
        valeur = self.tableau[0]
        
        # Décaler tous les éléments d'un cran vers la gauche
        for i in range(1, self.taille):
            self.tableau[i - 1] = self.tableau[i]
        
        self.taille -= 1
        return valeur

    def afficher(self):
        # Affiche les éléments de la file dans l'ordre FIFO
        print("File:", self.tableau[:self.taille])

# Exemple d'utilisation
file = FileTableauSimple(5)
file.enfiler(10)
file.enfiler(20)
file.enfiler(30)
file.afficher()  # Affiche : File: [10, 20, 30]

file.defiler()
file.afficher()  # Affiche : File: [20, 30]

file.enfiler(40)
file.enfiler(50)
file.afficher()  # Affiche : File: [20, 30, 40, 50]

# Tentative d'enfiler un élément lorsque la file est pleine
try:
    file.enfiler(60)
except OverflowError as e:
    print(e)  # Affiche : La file est pleine
