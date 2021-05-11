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

    def carte_use(self):
        if self.game.carte_use == "carte1":
            self.game.player_turn.carte1 = None
        elif self.game.carte_use == "carte2":
            self.game.player_turn.carte2 = None
        elif self.game.carte_use == "carte3":
            self.game.player_turn.carte3 = None


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
        self.game.list_crowd.crowd = self.game.list_crowd.liste_crowd[0]
        self.game.list_crowd.button_crowd = self.game.list_crowd.crowd.img
        self.game.list_crowd.change_crowd = False

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
        self.game.list_crowd.charge_crowd()
        self.carte_use()


class Sante_de_fer(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_de_fer.png")

    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()

class Adaptation(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/adaptation.png")

    def carte(self):
        choix_de_carte = random.randint(0, 14)
        if self.game.player_turn.carte1 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte1 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]
        elif self.game.player_turn.carte2 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte2 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]
        elif self.game.player_turn.carte3 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte3 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]

    def effect_carte(self):
        if self.game.player_turn.carte_gratuit:
            self.game.player_turn.carte_gratuit = False
            self.carte()
        if self.game.player_turn.carte_double:
            if self.game.player_turn.jauge_de_confiance >= 30:
                self.game.player_turn.carte_double = False
                self.carte()
                self.game.player_turn.jauge_de_confiance -= 30
        elif self.game.player_turn.jauge_de_confiance >= 15:
            self.carte()
            self.game.player_turn.jauge_de_confiance -= 15




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
        self.game.player_turn.bonus_publique = 0
        self.carte_use()

class Veteran(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/veteran.png")


    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()

class Sante_fragile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_fragile.png")


    def effect_carte(self):
        chance = random.randint(1, 2)
        if chance == 1:
            self.game.player_turn.jauge_de_confiance += 20
            self.carte_use()
        if chance == 2:
            self.game.player_turn.jauge_de_confiance -= 5
            self.carte_use()


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
        if self.game.player_not_turn.sexe == "F":
            self.game.player_not_turn.jauge_de_confiance -= 10
            self.game.player_turn.jauge_de_confiance += 10
        elif self.game.player_not_turn.sexe == "M":
            self.game.player_not_turn.jauge_de_confiance -= 5
            self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()


class Tonalite_virile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/tonalite_virile.png")
        

    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()

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
        self.game.player_turn.carte_gratuit = True
        self.carte_use()

#Femme
class Avantage_feminin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_feminin.png")


    def effect_carte(self):
        if self.game.player_not_turn.sexe == "M":
            self.game.player_not_turn.jauge_de_confiance -= 10
            self.game.player_turn.jauge_de_confiance += 10
        elif self.game.player_not_turn.sexe == "F":
            self.game.player_not_turn.jauge_de_confiance -= 5
            self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()

class Mauvaise_foi(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/mauvaise_foi.png")


    def effect_carte(self):
        if self.game.player_turn.carte_gratuit:
            self.game.player_turn.carte_gratuit = False
            self.game.player_not_turn.carte_double = True
        if self.game.player_turn.carte_double :
            if self.game.player_turn.jauge_de_confiance >= 10:
                self.game.player_not_turn.carte_double = True
                self.game.player_turn.carte_double = False
                self.game.player_turn.jauge_de_confiance -= 10
        elif self.game.player_turn.jauge_de_confiance >= 5 or self.game.player_turn.carte_gratuit :
            self.game.player_not_turn.carte_double = True
            self.game.player_turn.jauge_de_confiance -= 5
        

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
