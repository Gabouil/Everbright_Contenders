from caractere import Caractere
from random import randint



class Player2():
    def __init__(self,game):
        self.game = game
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
        self.number_carte1 = randint(0, 2)
        self.carte1 = self.caractere.list_cartes[self.number_carte1]
        self.number_carte2 = randint(3, 14)
        while self.number_carte2 == self.number_carte1:
            self.number_carte2 = randint(3, 14)
        self.carte2 = self.caractere.list_cartes[self.number_carte2]
        self.number_carte3 = randint(3, 14)
        while self.number_carte3 == self.number_carte2:
            self.number_carte3 = randint(3, 14)
        self.carte3 = self.caractere.list_cartes[self.number_carte3]
    def cc(self):
        pass