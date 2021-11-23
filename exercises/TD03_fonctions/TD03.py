#temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes
#Exercice 1:

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    jours = temps[0]
    heures = temps[1]
    minutes = temps[2]
    secondes = temps[3]

    joursEnseconde = jours * 3600 * 24
    heuresEnseconde = heures * 3600
    minutesEnseconde = minutes * 60 

    return joursEnseconde + heuresEnseconde + minutesEnseconde + secondes

temps = (3,23,1,34)
print(type(temps))
print(tempsEnSeconde(temps))



def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    return ((seconde // 3600) // 24, (seconde // 3600) % 24, (seconde // 60) % 60, seconde % 60)
    
temps = secondeEnTemps(100000)
print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici
#Exercice 2:

def afficheTemps(temps):
    if temps[0] == 1:
        print(temps[0], "jour", end=" ")
    elif temps[0] >= 2:
        print(temps[0], "jours", end=" ")

    if temps[1] == 1:
        print(temps[1], "heure", end=" ")
    elif temps[1] >= 2:
        print(temps[1], "heures", end=" ")
    
    if temps[2] == 1:
        print(temps[2], "minute", end=" ")
    elif temps[2] >= 2:
        print(temps[2], "minutes", end=" ")
    
    if temps[3] == 1:
        print(temps[3], "seconde", end=" ")
    elif temps[3] >= 2:
        print(temps[3], "secondes", end=" ")

afficheTemps((1,0,14,23))    


#Excercice 3:
#Partie 1:

import sys
def demandeTemps():
    temps1 = [0, 0, 0, 0]
    temps1[0] = int(input("\nsaisir jours : "))
    if (temps1[0] < 0):
        print("erreur")
        sys.exit()
    temps1[1] = int(input("saisir heures : "))
    if (temps1[1] < 0 or temps1[1] >= 24):
        print("erreur")
        sys.exit()
    temps1[2] = int(input("saisir minutes : "))
    if (temps1[2] < 0 or temps1[2] >= 60):
        print("erreur")
        sys.exit()
    temps1[3] = int(input("saisir secondes : "))
    if (temps1[3] < 0 or temps1[3] >= 60):
        print("erreur")
        sys.exit()
    
    return(temps1[0], temps1[1], temps1[2], temps1[3])
afficheTemps(demandeTemps())

#Partie 2:

def demandeTemps():
    temps2 = [0, 0, 0, 0]
    temps2[0] = int(input("\nsaisir jours : "))
    while (temps2[0] < 0):
        print("erreur")
        temps2[0] = int(input("saisir jours : "))
        
    temps2[1] = int(input("saisir heures : "))
    while temps2[1] < 0 or temps2[1] >= 24:
        print("erreur")
        temps2[1] = int(input("saisir heures : "))
        
    temps2[2] = int(input("saisir minutes : "))
    while (temps2[2] < 0 or temps2[2] >= 60):
        print("erreur")
        temps2[2] = int(input("saisir minutes : "))
    
    temps2[3] = int(input("saisir secondes : "))
    while (temps2[3] < 0 or temps2[3] >= 60):
        print("erreur")
        temps2[3] = int(input("saisir secondes : "))
        
    
    return (temps2)
afficheTemps(demandeTemps())

#Exercice 4:

def sommeTemps(temps1,temps2):

    print("")
    temps1EnSeconde = tempsEnSeconde(temps1)
    temps2EnSeconde = tempsEnSeconde(temps2)
    sommeEnSeconde = temps1EnSeconde + temps2EnSeconde

    return secondeEnTemps(sommeEnSeconde)
afficheTemps(sommeTemps((2,3,4,25),(5,22,57,1)))

#Exercice 5:

def proportionTemps(temps,proportion):
    
afficheTemps(proportionTemps((2,0,36,0),0.2))
        
    