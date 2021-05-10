import random
import pygame
from game import *

class Crowds :
    def __init__(self,  name, type):
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.crowdx, self.crowdy = self.mid_w, self.mid_h



class Erudits_et_guerriers(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Erudits_et_guerriers.png")


    def effect_crowd(self):
        pass
class Horslaloi_et_erudits(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_erudits.png")


    def effect_crowd(self):
        pass
class Horslaloi_et_guerriers(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_guerriers.png")
        

    def effect_crowd(self):
        pass
class Horslaloi_et_nobles(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Horslaloi_et_nobles.png")


    def effect_crowd(self):
        pass
class Nobles_et_erudits(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Nobles_et_erudits.png")


    def effect_crowd(self):
        pass
class Nobles_et_guerriers(Crowds):
    def __init__(self,  name, type):
        Crowds.__init__(self,  name, type)
        self.img = pygame.image.load("assets/crowd/Nobles_et_guerriers.png")


    def effect_crowd(self):
        pass


class Liste_crowd():
    def __init__(self, game):
        self.game = game
        self.Erudits_et_guerriers = Erudits_et_guerriers("Erudits_et_guerriers","à voir")
        self.Horslaloi_et_erudits = Horslaloi_et_erudits("Horslaloi_et_erudits","à voir")
        self.Horslaloi_et_guerriers = Horslaloi_et_guerriers("Horslaloi_et_guerriers","à voir")
        self.Horslaloi_et_nobles = Horslaloi_et_nobles("Horslaloi_et_nobles","à voir")
        self.Nobles_et_erudits = Nobles_et_erudits("Nobles_et_erudits","à voir")
        self.Nobles_et_guerriers = Nobles_et_guerriers("Nobles_et_guerriers","à voir")

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

    def alea_crowd(self):
        self.number_crowd = randint(0, 5)
        self.crowd = self.liste_crowd[self.number_crowd]
