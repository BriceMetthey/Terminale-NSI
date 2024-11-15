from Cellule import Cellule

class File:
    """structure de file"""
    def __init__(self):
        self.tete = None
        self.queue = None

    def est_vide(self):
        return self.tete is None

    def enfiler(self, x):
        c = Cellule(x, None)
        if self.est_vide():
            self.tete = c
        else:
            self.queue.suivante = c
        self.queue = c

    def defiler(self):
        if self.est_vide():
            raise IndexError("retirer sur une file vide")
        v = self.tete.valeur
        self.tete = self.tete.suivante
        if self.tete is None:
            self.queue = None
        return v
    



file_attente = File()

# Les élèves arrivent dans la file
file_attente.enfiler("Alice")
file_attente.enfiler("Bob")
file_attente.enfiler("Charlie")


# Les élèves sont servis un par un
print("Servi:", file_attente.defiler())  # Alice est servi
print("Servi:", file_attente.defiler())  # Bob est servi
print("Servi:", file_attente.defiler())  # Charlie est servi


# Essayer de sortir un élément d'une file vide

try:
    file_attente.defiler()
except IndexError as e:
    print(e)  # Affiche : La file est pleine
