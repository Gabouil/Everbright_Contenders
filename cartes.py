import random
import pygame
from game import *

class Cartes :
    def __init__(self, game,  name, type):
        self.game = game
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.cartex, self.cartey = self.mid_w, self.mid_h



class EXODIO(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self. EXODIO = pygame.image.load("assets/cartes/")
        self. EXODIO_rect = self. EXODIO.get_rect()
        self. EXODIO_rect.center = (self.cartex, self.cartey)

        self.chance_play = 1.2
        self.chance_effect = random.randint(1,4)

    def effect_carte(self):
        if self.chance_effect == 3 or self.chance_effect == 4:
            pass
        elif self.chance_effect == 1:
            pass
        elif self.chance_effect == 2:
            pass


# carte unique
#Liam
class True_story(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/true_story.png")


    def effect_carte(self):
        pass

class Peche_davarice(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/peche_davarice.png")

    def effect_carte(self):
        pass

class Gamin_des_rues(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/gamin_des_rues.png")

    def effect_carte(self):
        pass

#Ambre
class Secret_familial(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/secret_famillial.png")


    def effect_carte(self):
        pass

class Regard_enjoleur(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/regard_enjoleur.png")


    def effect_carte(self):
        pass

class Conseils_avisees(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/conseils_avisees.png")


    def effect_carte(self):
        pass

#Alfred
class Cest_pas_au_vieux_singe(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/cest_pas_au_vieux_singe.png")


    def effect_carte(self):
        pass

class Seconde_vie(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/second_vie.png")


    def effect_carte(self):
        pass

class Service_sur_mesure(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/service_sur_mesure.png")


    def effect_carte(self):
        pass

#Crystal
class Rhetorique_de_limperatrice(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/rhetorique_de_limperatrice.png")


    def effect_carte(self):
        pass

class Sombre_formule(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sombre_formule.png")

    def effect_carte(self):
        pass

class Influence_mystique(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/influence_mystique.png")


    def effect_carte(self):
        pass

#Cartes Comune
#Jeune
class Gout_du_risque(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/gout_du_risque.png")


    def effect_carte(self):
        pass

class Sante_de_fer(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_de_fer.png")


    def effect_carte(self):
        pass

class Adaptation(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/adaptation.png")


    def effect_carte(self):
        pass

class Esprit_vif(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/esprit_vif.png")

    def effect_carte(self):
        pass

#âgé
class Experience_de_lage(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/experience_de_lage.png")


    def effect_carte(self):
        pass

class Veteran(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/veteran.png")


    def effect_carte(self):
        pass

class Sante_fragile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_fragile.png")


    def effect_carte(self):
        pass

class Oeil_sage(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/oeil_sage.png")


    def effect_carte(self):
        pass

#Homme
class Avantage_masculin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_masculin.png")


    def effect_carte(self):
        pass

class Tonalite_virile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/tonalite_virile.png")
        

    def effect_carte(self):
        pass

class Sens_du_sacrifice(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sens_du_sacrifice.png")


    def effect_carte(self):
        pass

class Monotache(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/monotache.png")


    def effect_carte(self):
        pass

#Femme
class Avantage_feminin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_feminin.png")


    def effect_carte(self):
        pass

class Mauvaise_foi(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/mauvaise_foi.png")


    def effect_carte(self):
        pass

class Seduction(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/seduction.png")


    def effect_carte(self):
        pass

class Multitache(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/multitache.png")


    def effect_carte(self):
        pass

#Noble
class Opulence(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/opulence.png")


    def effect_carte(self):
        pass

class Hautes_relations(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/hautes_relation.png")


    def effect_carte(self):
        pass

class Mepris_du_fortune(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/mepris_du_fortune.png")

    def effect_carte(self):
        pass

class Pot_de_vin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/pot_de_vin.png")


    def effect_carte(self):
        pass

#Populaire
class Solidarite(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/solidarite.png")


    def effect_carte(self):
        pass

class Priere_misericordieuse(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/priere_misericordieuse.png")


    def effect_carte(self):
        pass

class Coup_de_chance(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/coup_de_chance.png")


    def effect_carte(self):
        pass

class Avantage_du_nombre(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_du_nombre.png")


    def effect_carte(self):
        pass
