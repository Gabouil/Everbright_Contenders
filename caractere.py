
from cartes import Cartes
from cartes import *
from game import *

class Caractere:
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        self.game = game
        self.firstname = firstname
        self.name = name
        self.classe_sociale = classe_sociale
        self.age = age
        self.sexe = sexe
        self.surnom = surnom
        self.list_cartes = []
        #

    def print_cartes(self):
        pass

    def print_boutdephrase(self):
        pass

    def choix_boutdephrase(self):
        pass

    def tour_du_joueur(self):
        pass

class Liam(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.img = pygame.image.load("assets/cartes/carte_liam.png")
        self.cartes = self.game.Liste_carte()
        self.list_cartes = [
            #Unique
            self.cartes.True_story,
            self.cartes.Peche_davarice,
            self.cartes.Gamin_des_rues,
            #Populaire
            self.cartes.Solidarite,
            self.cartes.Priere_misericordieuse,
            self.cartes.Coup_de_chance,
            self.cartes.Avantage_du_nombre,
            #Jeune
            self.cartes.Gout_du_risque,
            self.cartes.Sante_de_fer,
            self.cartes.Adaptation,
            self.cartes.Esprit_vif,
            #Homme
            self.cartes.Avantage_masculin,
            self.cartes.Tonalite_virile,
            self.cartes.Sens_du_sacrifice,
            self.cartes.Monotache

        ]
class Ambre(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.img = pygame.image.load("assets/cartes/carte_ambre.png")
        self.cartes = self.game.Liste_carte()
        self.list_cartes = [
            #Unique
            self.cartes.Secret_familial,
            self.cartes.Regard_enjoleur,
            self.cartes.Conseils_avisees,
            #Noble
            self.cartes.Opulence,
            self.cartes.Hautes_relations,
            self.cartes.Mepris_du_fortune,
            self.cartes.Pot_de_vin,
            #Jeune
            self.cartes.Gout_du_risque,
            self.cartes.Sante_de_fer,
            self.cartes.Adaptation,
            self.cartes.Esprit_vif,
            #Femme
            self.cartes.Avantage_feminin,
            self.cartes.Mauvaise_foi,
            self.cartes.Seduction,
            self.cartes.Multitache
            
        ]
class Alfred(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.cartes = self.game.Liste_carte()
        self.img = pygame.image.load("assets/cartes/carte_alfred.png")
        self.list_cartes = [
            #Unique
            self.cartes.Cest_pas_au_vieux_singe,
            self.cartes.Seconde_vie,
            self.cartes.Service_sur_mesure,
            #Noble
            self.cartes.Opulence,
            self.cartes.Hautes_relations,
            self.cartes.Mepris_du_fortune,
            self.cartes.Pot_de_vin,
            #âgé
            self.cartes.Experience_de_lage,
            self.cartes.Veteran,
            self.cartes.Sante_fragile,
            self.cartes.Oeil_sage,
            #Homme
            self.cartes.Avantage_masculin ,
            self.cartes.Tonalite_virile,
            self.cartes.Sens_du_sacrifice,
            self.cartes.Monotache
        ]
class Crystal(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.cartes = self.game.Liste_carte()
        self.img = pygame.image.load("assets/cartes/carte_crystal.png")
        self.list_cartes = [
            #Unique
            self.cartes.Rhetorique_de_limperatrice,
            self.cartes.Sombre_formule,
            self.cartes.Influence_mystique,
            #Populaire
            self.cartes.Solidarite,
            self.cartes.Priere_misericordieuse,
            self.cartes.Coup_de_chance,
            self.cartes.Avantage_du_nombre,
            #âgé
            self.cartes.Experience_de_lage,
            self.cartes.Veteran,
            self.cartes.Sante_fragile,
            self.cartes.Oeil_sage,

            #Femme
            self.cartes.Avantage_feminin,
            self.cartes.Mauvaise_foi,
            self.cartes.Seduction,
            self.cartes.Multitache
        ]
