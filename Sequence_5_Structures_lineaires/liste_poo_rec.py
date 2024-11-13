from Cellule import Cellule

def ajouter_en_queue_rec(node, valeur):
    if node.suivante is None:
        node.suivante = Cellule(valeur, None)
    else:
        ajouter_en_queue_rec(node.suivante, valeur)
            
            

def ajouter_rec(node, valeur, position):
    if position == 1 or node.suivante is None:
        node.suivante = Cellule(valeur, node.suivante)
    else:
        ajouter_rec(node.suivante, valeur, position - 1)
        
        

def supprimer_en_queue_rec(node):
    if node.suivante.suivante is None:
        node.suivante = None
    else:
        supprimer_en_queue_rec(node.suivante)



def supprimer_rec(node, position):
    if position == 1 and node.suivante is not None:
        node.suivante = node.suivante.suivante
    else:
        supprimer_rec(node.suivante, position - 1)



def chercher_rec(node, valeur):
    if node is None:
        return False
    if node.valeur == valeur:
        return True
    return chercher_rec(node.suivante, valeur)


def nieme_rec(node, position):
    if node is None:
        raise IndexError("Position hors de la liste")
    if position == 0:
        return node.valeur
    return nieme_rec(node.suivante, position - 1)


def parcourir_rec(node):
    if node is not None:
        print(node.valeur, end=' -> ')
        parcourir_rec(node.suivante)
    else:
        print('None')
        
        
def taille_rec(node):
    if node is None:
        return 0
    return 1 + taille_rec(node.suivante)


def renverser_rec(node, prev=None):
    if node is None:
        return prev
    next_node = node.suivante
    node.suivante = prev
    return renverser_rec(next_node, node)
