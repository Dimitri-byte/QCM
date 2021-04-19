# -*- coding: utf-8 -*-

# ------------------------------------------------------------------------------
# IMPORT
# ------------------------------------------------------------------------------
import yaml
import random
import os

# ------------------------------------------------------------------------------
# OBJECT
# ------------------------------------------------------------------------------

# Objet question
class Question:
    def __init__(self, id ):
        self.id = id
        self.description = qcm[id].get("question").get("description")
        self.correction = qcm[id].get("question").get("correction")
        self.positive = qcm[id].get("question").get("positive")
        self.negative = qcm[id].get("question").get("negative")

    def display(self):
        reponse= self.positive + self.negative
        random.shuffle(reponse)

        print( "---" )
        print( "| " + "QUESTION " + str(self.id) + " |" )
        print( "---" )

        print( self.description )
        print( "------" )

        cpt=0
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for i in reponse:
            print(alpha[cpt] + " : " + i)
            cpt+=1

        lettre = alpha.index(input("Réponse: "))
        print( "" )
        print("reponse choisie :" + reponse[lettre])

        if reponse[lettre] == self.positive[0]:
            print("succes")
        else:
            print("echec")
            with open("G:\Mon Drive\QCM\qcm_echec.yml", "r") as echecfile:
                fichier.write(qcm[id])

        print( "" )
        print( "---" )
        print(self.correction)

        print( "" )
        print( "" )
        print( "" )
        print( "" )
        input("appuyer sur une touche pour continuer")
        os.system('cls')

# ------------------------------------------------------------------------------
# FICHIER D ENTREE
# ------------------------------------------------------------------------------
inFile = r'G:\Mon Drive\QCM\qcm.yml'
# Lecture du fichier YAML
with open( inFile ) as file:
    qcm = yaml.full_load(file)

# ------------------------------------------------------------------------------
# CREATION DU TEST
# ------------------------------------------------------------------------------
cpt=0

while cpt <= len(qcm):
    Question(cpt).display()
    cpt+=1
