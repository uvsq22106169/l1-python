#Exercice 2


def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste = [n]
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            n = n * 3 + 1
        liste.append(int(n))
    return liste
print(syracuse(3))

#Exercice 3:

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range (2, n_max):
        y = syracuse(i)
        if y[-1] == 1:
            continue
    return True
print(testeConjecture(10000))

#Exercice 4 :

def tempsVol(n):
    """ Retourne le temps de vol de n """
    x = len(syracuse(n))
    return x

print("Le temps de vol de", 3, "est", tempsVol(3))

#Exercice 5 :
def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    x = [tempsVol]

print(tempsVolListe(100))