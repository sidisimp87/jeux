import  os

from carte import *

for fichier in os.listdir("cartes"):
    if fichier.endswith(".txt"):
        chemin=os.path.join("cartes",fichier)
        nom_carte=fichier[:-4]
        nom_carte=nom_carte[0].upper()+nom_carte[1:].lower()
        with open(chemin,'r') as fichier:
            contenu=fichier.read()
            carte=Carte(nom_carte,contenu)
        print(carte)

# for fichier in os.listdir("cartes"):




