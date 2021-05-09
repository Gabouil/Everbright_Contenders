from caractere import *
from random import randint


class Player1():
    def __init__(self):
        self.list_boutdephrase = [1, 2, 3]
        self.jauge_de_confiance = 0
        self.caractere = None
        self.carte1 = 0
        self.number_carte1 = 0
        self.carte2 = 0
        self.number_carte2 = 0
        self.carte3 = 0
        self.number_carte3 = 0


    def main_cartes(self):
        self.number_carte1 = randint(0, 3)
        self.carte1 = self.caractere.list_cartes[self.number_carte1]
        self.number_carte2 = randint(3, 18)
        self.carte2 = self.caractere.list_cartes[self.number_carte2]
        self.number_carte3 = randint(3, 18)
        self.carte3 = self.caractere.list_cartes[self.number_carte3]

    def cc(self):
        pass