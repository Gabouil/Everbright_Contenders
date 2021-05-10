import random
import pygame
from game import *

class Cartes :
    def __init__(self,  name, type):
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.cartex, self.cartey = self.mid_w, self.mid_h



class EXODIO(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
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
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/true_story.png")


    def effect_carte(self):
        pass

class Peche_davarice(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/peche_davarice.png")

    def effect_carte(self):
        pass

class Gamin_des_rues(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/gamin_des_rues.png")

    def effect_carte(self):
        pass

#Ambre
class Secret_familial(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/secret_famillial.png")


    def effect_carte(self):
        pass

class Regard_enjoleur(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/regard_enjoleur.png")


    def effect_carte(self):
        pass

class Conseils_avisees(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/conseils_avisees.png")


    def effect_carte(self):
        pass

#Alfred
class Cest_pas_au_vieux_singe(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/cest_pas_au_vieux_singe.png")


    def effect_carte(self):
        pass

class Seconde_vie(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/second_vie.png")


    def effect_carte(self):
        pass

class Service_sur_mesure(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/service_sur_mesure.png")


    def effect_carte(self):
        pass

#Crystal
class Rhetorique_de_limperatrice(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/rhetorique_de_limperatrice.png")


    def effect_carte(self):
        pass

class Sombre_formule(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/sombre_formule.png")

    def effect_carte(self):
        pass

class Influence_mystique(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/influence_mystique.png")


    def effect_carte(self):
        pass

#Cartes Comune
#Jeune
class Gout_du_risque(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/gout_du_risque.png")


    def effect_carte(self):
        pass

class Sante_de_fer(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_de_fer.png")


    def effect_carte(self):
        pass

class Adaptation(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/adaptation.png")


    def effect_carte(self):
        pass

class Esprit_vif(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/esprit_vif.png")

    def effect_carte(self):
        pass

#âgé
class Experience_de_lage(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/experience_de_lage.png")


    def effect_carte(self):
        pass

class Veteran(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/veteran.png")


    def effect_carte(self):
        pass

class Sante_fragile(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_fragile.png")


    def effect_carte(self):
        pass

class Oeil_sage(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/oeil_sage.png")


    def effect_carte(self):
        pass

#Homme
class Avantage_masculin(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_masculin.png")


    def effect_carte(self):
        pass

class Tonalite_virile(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/tonalite_virile.png")
        

    def effect_carte(self):
        pass

class Sens_du_sacrifice(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/sens_du_sacrifice.png")


    def effect_carte(self):
        pass

class Monotache(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/monotache.png")


    def effect_carte(self):
        pass

#Femme
class Avantage_feminin(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_feminin.png")


    def effect_carte(self):
        pass

class Mauvaise_foi(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/mauvaise_foi.png")


    def effect_carte(self):
        pass

class Seduction(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/seduction.png")


    def effect_carte(self):
        pass

class Multitache(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/multitache.png")


    def effect_carte(self):
        pass

#Noble
class Opulence(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/opulence.png")


    def effect_carte(self):
        pass

class Hautes_relations(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/hautes_relation.png")


    def effect_carte(self):
        pass

class Mepris_du_fortune(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/mepris_du_fortune.png")

    def effect_carte(self):
        pass

class Pot_de_vin(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/pot_de_vin.png")


    def effect_carte(self):
        pass

#Populaire
class Solidarite(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/solidarite.png")


    def effect_carte(self):
        pass

class Priere_misericordieuse(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/priere_misericordieuse.png")


    def effect_carte(self):
        pass

class Coup_de_chance(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/coup_de_chance.png")


    def effect_carte(self):
        pass

class Avantage_du_nombre(Cartes):
    def __init__(self,  name, type):
        Cartes.__init__(self,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_du_nombre.png")


    def effect_carte(self):
        pass


class Liste_carte():
    def __init__(self):
        #Liam
        self.True_story = True_story( "True story", "Unique")
        self.Peche_davarice = Peche_davarice( "Peche davarice", "Unique")
        self.Gamin_des_rues = Gamin_des_rues( "Gamin des rues", "Unique")
        #Ambre
        self.Secret_familial = Secret_familial( "Secret familial", "Unique")
        self.Regard_enjoleur = Regard_enjoleur(  "Regard enjoleur", "Unique")
        self.Conseils_avisees = Conseils_avisees(  "Conseils avisees", "Unique")
        #Alfred
        self.Cest_pas_au_vieux_singe = Cest_pas_au_vieux_singe( "Cest pas au vieux singe", "Unique")
        self.Seconde_vie = Seconde_vie( "Seconde vie", "Unique")  
        self.Service_sur_mesure = Service_sur_mesure( "Service sur mesure", "Unique") 
        #Crystal
        self.Rhetorique_de_limperatrice = Rhetorique_de_limperatrice( "Rhetorique de limperatrice", "Unique")
        self.Sombre_formule = Sombre_formule(  "Sombre formule", "Unique") 
        self.Influence_mystique = Influence_mystique( "Influence mystique", "Unique")    
        #Cartes Comune
        #Jeune
        self.Gout_du_risque = Gout_du_risque(  "Gout du risque", "Jeune") 
        self.Sante_de_fer = Sante_de_fer (  "Sante de fer", "Jeune")
        self.Adaptation = Adaptation(  "Adaptation ", "Jeune")
        self.Esprit_vif = Esprit_vif(  "Esprit vif ", "Jeune")
        #âgé
        self.Experience_de_lage = Experience_de_lage( "Experience de lage ", "âgé")
        self.Veteran = Veteran( " Veteran ", "âgé")
        self.Sante_fragile = Sante_fragile( " Sante fragile ", "âgé")  
        self.Oeil_sage = Oeil_sage(  " Oeil sage", "âgé")    
        #Homme
        self.Avantage_masculin = Avantage_masculin(  "Avantage masculin", "Homme")
        self.Tonalite_virile = Tonalite_virile (  "Tonalite virile", "Homme") 
        self.Sens_du_sacrifice = Sens_du_sacrifice( "Sens du sacrifice", "Homme") 
        self.Monotache = Monotache( "Monotache", "Homme")
        #Femme
        self.Avantage_feminin = Avantage_feminin( "Avantage feminin", "Femme") 
        self.Mauvaise_foi = Mauvaise_foi( "Mauvaise foi", "Femme")
        self.Seduction = Seduction( "Seduction", "Femme") 
        self.Multitache = Multitache(  "Multitache", "Femme")  
        #Noble
        self.Opulence = Opulence( "Opulence", "Noble") 
        self.Hautes_relations = Hautes_relations(  "Hautes relations", "Noble")     
        self.Mepris_du_fortune = Mepris_du_fortune(  "Mepris du fortune", "Noble")   
        self.Pot_de_vin = Pot_de_vin(  "Pot de vin", "Noble")   
        #Populaire
        self.Solidarite = Solidarite( "Solidarite", "Populaire") 
        self.Priere_misericordieuse = Priere_misericordieuse(  "Priere misericordieuse", "Populaire")     
        self.Coup_de_chance = Coup_de_chance(  "Coup de chance", "Populaire") 
        self.Avantage_du_nombre = Avantage_du_nombre(  "Avantage du nombre", "Populaire")    

