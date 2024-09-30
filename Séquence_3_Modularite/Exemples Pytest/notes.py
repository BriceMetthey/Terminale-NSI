def calcul_moyenne(notes):
    somme = 0
    for note in notes:
        somme += note
    moyenne = 0
    if len(notes) != 0 :
        moyenne = somme / len(notes)
    return moyenne

def est_recu(notes):
    moyenne = calcul_moyenne(notes)
    if moyenne >= 10:
        return True
    else:
        return False