import random
import pygame
from game import *

class Cartes :
    def __init__(self, game, name, type):
        self.game = game
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.cartex, self.cartey = self.mid_w, self.mid_h



class EXODIO(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
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
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.True_story = pygame.image.load("assets/cartes/true_story.png")
        self.True_story_rect = self.True_story.get_rect()
        self.True_story_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Peche_davarice(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Peche_davarice = pygame.image.load("assets/cartes/peche_davarice.png")
        self.Peche_davarice_rect = self.Peche_davarice.get_rect()
        self.Peche_davarice_rect.center = (self.cartex, self.cartey)

    def effect_carte(self):
        pass

class Gamin_des_rues(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Gamin_des_rues = pygame.image.load("assets/cartes/gamin_des_rues.png")
        self.Gamin_des_rues_rect = self.Gamin_des_rues.get_rect()
        self.Gamin_des_rues_rect.center = (self.cartex, self.cartey)

    def effect_carte(self):
        pass

#Ambre
class Secret_familial(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Secret_familial = pygame.image.load("assets/cartes/secret_famillial.png")
        self.Secret_familial_rect = self.Secret_familial.get_rect()
        self.Secret_familial_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Regard_enjoleur(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Regard_enjoleur = pygame.image.load("assets/cartes/regard_enjoleur.png")
        self.Regard_enjoleur_rect = self.Regard_enjoleur.get_rect()
        self.Regard_enjoleur_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Conseils_avisees(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Conseils_avisees = pygame.image.load("assets/cartes/conseils_avisees.png")
        self.Conseils_avisees_rect = self.Conseils_avisees.get_rect()
        self.Conseils_avisees_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Alfred
class Cest_pas_au_vieux_singe(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Cest_pas_au_vieux_singe = pygame.image.load("assets/cartes/cest_pas_au_vieux_singe.png")
        self.Cest_pas_au_vieux_singe_rect = self.Cest_pas_au_vieux_singe.get_rect()
        self.Cest_pas_au_vieux_singe_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Seconde_vie(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Seconde_vie = pygame.image.load("assets/cartes/second_vie.png")
        self.Seconde_vie_rect = self.Seconde_vie.get_rect()
        self.Seconde_vie_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Service_sur_mesure(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Service_sur_mesure = pygame.image.load("assets/cartes/service_sur_mesure.png")
        self.Service_sur_mesure_rect = self.Service_sur_mesure.get_rect()
        self.Service_sur_mesure_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Crystal
class Rhetorique_de_limperatrice(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Rhetorique_de_limperatrice = pygame.image.load("assets/cartes/rhetorique_de_limperatrice.png")
        self.Rhetorique_de_limperatrice_rect = self.Rhetorique_de_limperatrice.get_rect()
        self.Rhetorique_de_limperatrice_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Sombre_formule(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Sombre_formule = pygame.image.load("assets/cartes/sombre_formule.png")
        self.Sombre_formule_rect = self.Sombre_formule.get_rect()
        self.Sombre_formule_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Influence_mystique(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Influence_mystique = pygame.image.load("assets/cartes/influence_mystique.png")
        self.Influence_mystique_rect = self.Influence_mystique.get_rect()
        self.Influence_mystique_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Cartes Comune
#Jeune
class Gout_du_risque(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Gout_du_risque = pygame.image.load("assets/cartes/gout_du_risque.png")
        self.Gout_du_risque_rect = self.Gout_du_risque.get_rect()
        self.Gout_du_risque_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Sante_de_fer(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Sante_de_fer = pygame.image.load("assets/cartes/sante_de_fer.png")
        self.Sante_de_fer_rect = self.Sante_de_fer.get_rect()
        self.Sante_de_fer_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Adaptation(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Adaptation = pygame.image.load("assets/cartes/adaptation.png")
        self.Adaptation_rect = self.Adaptation.get_rect()
        self.Adaptation_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Esprit_vif(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Esprit_vif = pygame.image.load("assets/cartes/esprit_vif.png")
        self.Esprit_vif_rect = self.Esprit_vif.get_rect()
        self.Esprit_vif_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#âgé
class Experience_de_lage(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Experience_de_lage = pygame.image.load("assets/cartes/experience_de_lage.png")
        self.Experience_de_lage_rect = self.Experience_de_lage.get_rect()
        self.Experience_de_lage_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Veteran(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Veteran = pygame.image.load("assets/cartes/veteran.png")
        self.Veteran_rect = self.Veteran.get_rect()
        self.Veteran_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Sante_fragile(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Sante_fragile = pygame.image.load("assets/cartes/sante_fragile.png")
        self.Sante_fragile_rect = self.Sante_fragile.get_rect()
        self.Sante_fragile_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Oeil_sage(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Oeil_sage = pygame.image.load("assets/cartes/oeil_sage.png")
        self.Oeil_sage_rect = self.Oeil_sage.get_rect()
        self.Oeil_sage_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Homme
class Avantage_masculin(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Avantage_masculin = pygame.image.load("assets/cartes/avantage_masculin.png")
        self.Avantage_masculin_rect = self.Avantage_masculin.get_rect()
        self.Avantage_masculin_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Tonalite_virile(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Tonalite_virile = pygame.image.load("assets/cartes/tonalite_virile.png")
        self.Tonalite_virile_rect = self.Tonalite_virile.get_rect()
        self.Tonalite_virile_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Sens_du_sacrifice(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Sens_du_sacrifice = pygame.image.load("assets/cartes/sens_du_sacrifice.png")
        self.Sens_du_sacrifice_rect = self.Sens_du_sacrifice.get_rect()
        self.Sens_du_sacrifice_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Monotache(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Monotache = pygame.image.load("assets/cartes/monotache.png")
        self.Monotache_rect = self.Monotache.get_rect()
        self.Monotache_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Femme
class Avantage_feminin(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Avantage_feminin = pygame.image.load("assets/cartes/avantage_feminin.png")
        self.Avantage_feminin_rect = self.Avantage_feminin.get_rect()
        self.Avantage_feminin_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Mauvaise_foi(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Mauvaise_foi = pygame.image.load("assets/cartes/mauvaise_foi.png")
        self.Mauvaise_foi_rect = self.Mauvaise_foi.get_rect()
        self.Mauvaise_foi_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Seduction(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Seduction = pygame.image.load("assets/cartes/seduction.png")
        self.Seduction_rect = self.Seduction.get_rect()
        self.Seduction_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Multitache(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Multitache = pygame.image.load("assets/cartes/multitache.png")
        self.Multitache_rect = self.Multitache.get_rect()
        self.Multitache_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Noble
class Opulence(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Opulence = pygame.image.load("assets/cartes/opulence.png")
        self.Opulence_rect = self.Opulence.get_rect()
        self.Opulence_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Hautes_relations(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Hautes_relations = pygame.image.load("assets/cartes/hautes_relation.png")
        self.Hautes_relations_rect = self.Hautes_relations.get_rect()
        self.Hautes_relations_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Mepris_du_fortune(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Mepris_du_fortune = pygame.image.load("assets/cartes/mepris_du_fortune.png")
        self.Mepris_du_fortune_rect = self.Mepris_du_fortune.get_rect()
        self.Mepris_du_fortune_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Pot_de_vin(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Pot_de_vin = pygame.image.load("assets/cartes/pot_de_vin.png")
        self.Pot_de_vin_rect = self.Pot_de_vin.get_rect()
        self.Pot_de_vin_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

#Populaire
class Solidarite(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Solidarite = pygame.image.load("assets/cartes/solidarite.png")
        self.Solidarite_rect = self.Solidarite.get_rect()
        self.Solidarite_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Priere_misericordieuse(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Priere_misericordieuse = pygame.image.load("assets/cartes/priere_misericordieuse.png")
        self.Priere_misericordieuse_rect = self.Priere_misericordieuse.get_rect()
        self.Priere_misericordieuse_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Coup_de_chance(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Coup_de_chance = pygame.image.load("assets/cartes/coup_de_chance.png")
        self.Coup_de_chance_rect = self.Coup_de_chance.get_rect()
        self.Coup_de_chance_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass

class Avantage_du_nombre(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game, name, type)
        self.Avantage_du_nombre = pygame.image.load("assets/cartes/avantage_du_nombre.png")
        self.Avantage_du_nombre_rect = self.Avantage_du_nombre.get_rect()
        self.Avantage_du_nombre_rect.center = (self.cartex, self.cartey)


    def effect_carte(self):
        pass


class Liste_carte():
    def __init__(self):
        self.True_story = True_story(Game, "True_story", "Unique")
        self.Peche_davarice = Peche_davarice(Game, "Peche davarice", "Unique")
        self.Gamin_des_rues = Gamin_des_rues(Game, "Gamin_des_rues", "Unique")
