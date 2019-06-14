"""Fonction necessaire au fonctionnement du jeu"""
def etat_chaine(chaine):

    position_robot=tuple(); position_porte=tuple(); position_murs =list()

    for lig,str_1 in enumerate(chaine.split("\n")):
        for col, str_2 in enumerate(str_1):
            # print(col, ' ', str_2)
            if str_2 =="X":
                position_robot=(col,lig)
            if str_2 == "0":
                position_murs.append((col,lig))
            if str_2 == "U":
                position_porte= (col,lig)
    return position_robot,position_porte,position_murs

