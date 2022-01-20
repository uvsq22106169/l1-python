#Exercice 
carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]

def afficheCarre(carre):
    Affiche la liste à 2 dimensions carre comme un carré
    for i in range(len(carre)):
        for j in range(len(carre)):
            print(carre[i][j], end= " ")
        print(" ")
        

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

