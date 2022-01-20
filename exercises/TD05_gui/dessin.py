import tkinter as tk
def affichage(texte):
    """ Modifie le texte d'un label. """
    label.config(text=texte)

racine = tk.Tk()
label = tk.Label(racine, text="", padx=20, pady=20, font = ("helvetica", "20"))
label.grid(row=0, column=0, columnspan=2)
canvas = tk.Canvas(racine, bg = "black", height=600, width=600 )
bouton = tk.Button(racine, text="choisir une couleur", command=affichage, font= ("Helvetica", "20"))
bouton2 = tk.Button(racine, text= "Cercle", command=affichage, font= ("Helvetica", "20"))
bouton3 = tk.Button(racine, text= "Carré", command=affichage, font= ("Helvetica", "20"))
bouton4 = tk.Button(racine, text= "Croix", command=affichage, font= ("Helvetica", "20"))



bouton.grid(row = 0, column= 2)
bouton2.grid(row=1, column=0)
bouton3.grid(row=2, column= 0)
bouton4.grid(row=3, column= 0)
canvas.grid(row=2,column=2)
racine.mainloop()