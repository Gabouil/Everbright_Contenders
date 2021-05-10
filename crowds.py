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
    def __init__(self):
        self.Erudits_et_guerriers = Erudits_et_guerriers("Erudits_et_guerriers","à voir")
        self.Horslaloi_et_erudits = Horslaloi_et_erudits("Horslaloi_et_erudits","à voir")
        self.Horslaloi_et_guerriers = Horslaloi_et_guerriers("Horslaloi_et_guerriers","à voir")
        self.Horslaloi_et_nobles = Horslaloi_et_nobles("Horslaloi_et_nobles","à voir")
        self.Nobles_et_erudits = Nobles_et_erudits("Nobles_et_erudits","à voir")
        self.Nobles_et_guerriers = Nobles_et_guerriers("Nobles_et_guerriers","à voir")
