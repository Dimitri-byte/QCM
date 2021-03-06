# -*- coding: utf-8 -*-


# ------------------------------------------------------------------------------
# IMPORT
# ------------------------------------------------------------------------------
import yaml
import random
import os
from colorama import Fore, Back, Style

# ------------------------------------------------------------------------------
# OBJECT
# ------------------------------------------------------------------------------

class Question:
    def __init__(self, id, qcm ):
        self.id = id
        self.qcm = qcm
        self.description = self.qcm[id].get("question").get("description")
        self.correction = self.qcm[id].get("question").get("correction")
        self.positive = self.qcm[id].get("question").get("positive")
        self.negative = self.qcm[id].get("question").get("negative")

    def Continue(self):
        print( "\n---" )
        print("CORRECTION")
        print( "---" )
        print(self.correction)

        print( "\n\n\n\n------" )
        input("appuyer sur une touche pour continuer")
        print(Style.RESET_ALL)
        os.system('cls')


    def display(self, listeError):
        reponse= self.positive + self.negative
        random.shuffle(reponse)

        print( "---" )
        print( "| " + "QUESTION " + str(self.id) + " |" )
        print( "---" )

        print( "\n" )
        print( self.description )
        print( "\n\n--------------------------------" )

        cpt=0
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",""]
        for i in reponse:
            print(alpha[cpt] + " : " + i)
            cpt+=1


        print( "--------------------------------" )
        drag = False
        while drag == False:
            rep = str(input("Réponse: "))
            for i in alpha:
                if rep == i:
                    drag = True

        if rep == "":
            listeError.append(self.qcm[self.id])
            self.Continue()
        elif alpha.index(rep) >= len(reponse) :
            listeError.append(self.qcm[self.id])
            self.Continue()
        else:
            lettre = alpha.index(rep)
            print("reponse choisie :" + reponse[lettre])
            if reponse[lettre] == self.positive[0]:
                print(Fore.GREEN + "\n\n\nCORRECT")
                self.Continue()
            else:
                print(Fore.RED + "\n\n\nECHEC")
                # with open(r'G:\Mon Drive\QCM\qcm_echec1.yml' , "w") as echecfile1:
                #     yaml.dump(qcm[self.id], echecfile1)
                listeError.append(self.qcm[self.id])
                self.Continue()



# ------------------------------------------------------------------------------
# FICHIER D ENTREE
# ------------------------------------------------------------------------------
inFile = r'G:\Mon Drive\QCM\qcm.yml'
echecfile=r'G:\Mon Drive\QCM\qcm_echec.yml'
# Lecture du fichier YAML
with open( inFile , encoding='utf8' ) as file:
    qcm = yaml.full_load(file)

# ------------------------------------------------------------------------------
# CREATION DU TEST
# ------------------------------------------------------------------------------

cpt=0
listeError=[]
random.shuffle(qcm)

while cpt < len(qcm):
    Question(cpt, qcm ).display(listeError)
    cpt+=1

with open(echecfile, "w", encoding='utf-8') as echecfile1:
    yaml.dump(listeError, echecfile1)
