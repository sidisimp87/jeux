"""Classe sur les cartes !"""

from fonction import *

class Carte:
    def __init__(self,nom,chaine):
        self.nom=nom
        self.chaine = chaine
        self.plan=chaine.replace("X"," ")
        self.robot=etat_chaine(chaine)[0]
        self.succes = etat_chaine(chaine)[1]
        self.murs = etat_chaine(chaine)[2]
        self.larg=len(chaine.split('\n')[0])
        self.long = len(chaine.split('\n'))


        # print(self.nom,'\n')
        # print(self.chaine,'\n')
        # print(self.plan)
        # print('Le robot = ',self.robot)
        # print('Le succes = ', self.succes)
        # print('Le mur = ', self.murs)
        # print('Le larg = ', self.larg)
        # print('Le long = ', self.long)


    def __repr__(self):
        return "<Carte {}>".format(self.nom)










