#Exercice 
"""carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]

def afficheCarre(carre):
    Affiche la liste à 2 dimensions carre comme un carré
    for i in range(len(carre)):
        for j in range(len(carre)):
            print(carre[i][j], end= " ")
        print(" ")
        

afficheCarre(carre_mag)
#afficheCarre(carre_pas_mag)"""





base = [[200, -42, 312], [-51,-22, -3, 80, 23]]

def bilan_mensuel (bilan):
    L = []
    L1 = []
    for i in range(len(bilan)):
        total_depenses = 0
        total_rentree  = 0 
        for j in range (len(bilan)):
            if base[j][i] > 0:
                total_depenses += bilan[j][i]
            else :
                total_rentree += bilan[j][i]
        L.append(total_rentree)
        L1.append(total_depenses)
        
    

    print (L)
bilan_mensuel(base)