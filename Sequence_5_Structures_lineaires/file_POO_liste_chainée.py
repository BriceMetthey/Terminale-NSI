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
        
f = File()
f.enfiler(1)
f.enfiler(2)
f.enfiler(3)
assert f.defiler() == 1
assert f.defiler() == 2
assert f.defiler() == 3