import random
import pygame
from game import *

class Crowds :
    def __init__(self, game,  name):
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.game = game
        self.name = name
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.crowdx, self.crowdy = self.mid_w, self.mid_h
        self.bonus_confiance = 15
        self.bonus_publique = 1.5



class Erudits_et_guerriers(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Erudits_et_guerriers.png")


    def effect_crowd(self):
        if self.game.player1.caractere == self.game.liam:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.liam:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance

class Horslaloi_et_erudits(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_erudits.png")


    def effect_crowd(self):
        if self.game.player1.caractere == self.game.ambre:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.ambre:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance

class Horslaloi_et_guerriers(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_guerriers.png")
        

    def effect_crowd(self):
        if self.game.player1.caractere == self.game.crystal or self.game.player1.caractere == self.game.liam:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.crystal or self.game.player1.caractere == self.game.liam:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance

class Horslaloi_et_nobles(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_nobles.png")


    def effect_crowd(self):
        if self.game.player1.caractere == self.game.crystal:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.crystal:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance

class Nobles_et_erudits(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Nobles_et_erudits.png")


    def effect_crowd(self):
        if self.game.player1.caractere == self.game.alfred or self.game.player1.caractere == self.game.ambre:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.alfred or self.game.player2.caractere == self.game.ambre:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance

class Nobles_et_guerriers(Crowds):
    def __init__(self, game,  name):
        Crowds.__init__(self, game,  name)
        self.img = pygame.image.load("assets/crowd/Nobles_et_guerriers.png")


    def effect_crowd(self):
        if self.game.player1.caractere == self.game.alfred:
            self.game.player1.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player1.jauge_de_confiance = self.bonus_confiance
        if self.game.player2.caractere == self.game.alfred:
            self.game.player2.bonus_publique = self.bonus_publique
            if self.game.turn == 1:
                self.game.player2.jauge_de_confiance = self.bonus_confiance




class Liste_crowd():
    def __init__(self, game):
        self.game = game
        self.change_crowd = True
        self.Erudits_et_guerriers = Erudits_et_guerriers(game,"Erudits_et_guerriers")
        self.Horslaloi_et_erudits = Horslaloi_et_erudits(game,"Horslaloi_et_erudits")
        self.Horslaloi_et_guerriers = Horslaloi_et_guerriers(game,"Horslaloi_et_guerriers")
        self.Horslaloi_et_nobles = Horslaloi_et_nobles(game,"Horslaloi_et_nobles")
        self.Nobles_et_erudits = Nobles_et_erudits(game,"Nobles_et_erudits")
        self.Nobles_et_guerriers = Nobles_et_guerriers(game,"Nobles_et_guerriers")

        self.liste_crowd = [
            self.Erudits_et_guerriers,
            self.Horslaloi_et_erudits,
            self.Horslaloi_et_guerriers,
            self.Horslaloi_et_nobles,
            self.Nobles_et_erudits,
            self.Nobles_et_guerriers,
        ]

    def charge_crowd(self):
        self.alea_crowd()
        self.button_crowd = self.crowd.img
        self.button_crowd_rect = self.button_crowd.get_rect()
        self.button_crowd_rect.center = (self.game.crowdx, self.game.crowdy)
        self.crowd.effect_crowd()

    def alea_crowd(self):
        self.number_crowd = randint(0, 5)
        self.crowd = self.liste_crowd[self.number_crowd]
