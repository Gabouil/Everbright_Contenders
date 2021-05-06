
from cartes import Cartes
class Caractere:
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        self.firstname = firstname
        self.name = name
        self.classe_sociale = classe_sociale
        self.age = age
        self.sexe = sexe
        self.list_cartes = []
    
    def distribution_cartes(self):
        nbrcartes = list_cartes[4]
        for i in range(len(list_cartes)):
            if list_cartes[i] >= nbrcartes :
                nbrcartes = liste[i]
        return nbrcartes


    def choix_cartes(self):
        # self.list_cartes()
        print("Choisissez une carte:")
        choix = int(input())
        # self.print_cartes(self.list_cartes[choix])
        print(self.list_cartes[choix])
        self.list_cartes.pop(choix)
        print(self.list_cartes)

    def print_cartes(self):

        for i in range(0, len(self.list_cartes), 1):
            print(i, ":", self.list_cartes[i])

    def print_boutdephrase(self):

        for i in range(0, len(self.list_boutdephrase), 1):
            print(i, ":", self.list_boutdephrase[i])

    def choix_boutdephrase(self):
        # self.list_boutdephrase()
        print("Choisissez un bout de phrase:")
        choix2 = int(input())
        self.print_cartes(self.list_cartes[choix2])

    def tour_du_joueur(self):
        print("Vous voulez faire quoi?")
        print("1: choix de carte")
        print("2:  choix du boutdephrase")
        choix = int(input())
        if choix == 1:
            carte_choisie = self.choix_cartes()
            return carte_choisie
        elif choix == 2:
            boutdephrase_choisie = self.choix_boutdephrase()
            # return boutdephrase_choisie
            
            
            
            