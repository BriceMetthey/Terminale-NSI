from pile_liste_chainee import Cellule, Pile

def verifier_parenthesage(expression):
    pile = Pile()  # Création de la pile

    for caractere in expression:
        if caractere in "({[":  # Si c'est une parenthèse ouvrante
            pile.empiler(caractere)  # On l'ajoute à la pile
        elif caractere == ")":
            if pile.est_vide() or pile.depiler() != "(":  # Vérifie la correspondance avec "("
                return False
        elif caractere == "}":
            if pile.est_vide() or pile.depiler() != "{":  # Vérifie la correspondance avec "{"
                return False
        elif caractere == "]":
            if pile.est_vide() or pile.depiler() != "[":  # Vérifie la correspondance avec "["
                return False

    # Si la pile est vide, l'expression est bien parenthésée
    return pile.est_vide()


assert verifier_parenthesage("(a + b) * (c + d)") == True   # Retourne True
assert verifier_parenthesage("(a + b * (c - d)") == False  # Retourne False
assert verifier_parenthesage("([a + b] * {c - d})") == True # Retourne True
assert verifier_parenthesage("([a + b] * {c - d}") == False # Retourne False