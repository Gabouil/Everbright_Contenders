
from cartes import Cartes
from cartes import *
from game import *

class Caractere:
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        self.firstname = firstname
        self.name = name
        self.classe_sociale = classe_sociale
        self.age = age
        self.sexe = sexe
        self.list_cartes = []
    
    def distribution_cartes(self):
        nbrcartes = list_cartes[4]
        for i in range(len(list_cartes)):
            if list_cartes[i] >= nbrcartes :
                nbrcartes = liste[i]
        return nbrcartes


    def choix_cartes(self):
        # self.list_cartes()
        print("Choisissez une carte:")
        choix = int(input())
        # self.print_cartes(self.list_cartes[choix])
        print(self.list_cartes[choix])
        self.list_cartes.pop(choix)
        print(self.list_cartes)

    def print_cartes(self):

        for i in range(0, len(self.list_cartes), 1):
            print(i, ":", self.list_cartes[i])

    def print_boutdephrase(self):

        for i in range(0, len(self.list_boutdephrase), 1):
            print(i, ":", self.list_boutdephrase[i])

    def choix_boutdephrase(self):
        # self.list_boutdephrase()
        print("Choisissez un bout de phrase:")
        choix2 = int(input())
        self.print_cartes(self.list_cartes[choix2])

    def tour_du_joueur(self):
        print("Vous voulez faire quoi?")
        print("1: choix de carte")
        print("2:  choix du boutdephrase")
        choix = int(input())
        if choix == 1:
            carte_choisie = self.choix_cartes()
            return carte_choisie
        elif choix == 2:
            boutdephrase_choisie = self.choix_boutdephrase()
            # return boutdephrase_choisie

class Liam(Caractere):
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        Caractere.__init__(self, firstname, name, classe_sociale, age, sexe)
        self.cartes = Liste_carte()
        self.list_cartes = [
            #Unique
            self.cartes.True_story,
            self.Peche_davarice,
            self.Gamin_des_rues,
            #Populaire
            self.Solidarite,
            self.Priere_misericordieuse,
            self.Coup_de_chance,
            self.Avantage_du_nombre,
            #Jeune
            self.Gout_du_risque,
            self.Sante_de_fer,
            self.Adaptation,
            self.Esprit_vif,  
            #Homme
            self.Avantage_masculin ,
            self.Tonalite_virile, 
            self.Sens_du_sacrifice,
            self.Monotache 

        ]
class Ambre(Caractere):
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        Caractere.__init__(self, firstname, name, classe_sociale, age, sexe)
        self.cartes = Liste_carte()
        self.list_cartes = [
            #Unique
            self.Secret_familial, 
            self.Regard_enjoleur,
            self.Conseils_avisees,
            #Noble
            self.Opulence, 
            self.Hautes_relations,
            self.Mepris_du_fortune,
            self.Pot_de_vin, 
            #Jeune
            self.Gout_du_risque,
            self.Sante_de_fer,
            self.Adaptation,
            self.Esprit_vif, 
            #Femme
            self.Avantage_feminin,
            self.Mauvaise_foi,
            self.Seduction,
            self.Multitache 
            
        ]
class Alfred(Caractere):
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        Caractere.__init__(self, firstname, name, classe_sociale, age, sexe)
        self.cartes = Liste_carte()
        self.list_cartes = [
            #Unique
            self.Cest_pas_au_vieux_singe,  
            self.Seconde_vie,   
            self.Service_sur_mesure,
            #Noble
            self.Opulence, 
            self.Hautes_relations,
            self.Mepris_du_fortune,
            self.Pot_de_vin,
            #âgé
            self.Experience_de_lage, 
            self.Veteran, 
            self.Sante_fragile,
            self.Oeil_sage,
            #Homme
            self.Avantage_masculin ,
            self.Tonalite_virile, 
            self.Sens_du_sacrifice,
            self.Monotache 
        ]
class Crystal(Caractere):
    def __init__(self, firstname, name, classe_sociale, age, sexe):
        Caractere.__init__(self, firstname, name, classe_sociale, age, sexe)
        self.cartes = Liste_carte()
        self.list_cartes = [
            #Unique
            self.Rhetorique_de_limperatrice,
            self.Sombre_formule, 
            self.Influence_mystique,
            #Populaire
            self.Solidarite,
            self.Priere_misericordieuse,
            self.Coup_de_chance,
            self.Avantage_du_nombre,
            #âgé
            self.Experience_de_lage, 
            self.Veteran, 
            self.Sante_fragile,
            self.Oeil_sage, 

            #Femme
            self.Avantage_feminin,
            self.Mauvaise_foi,
            self.Seduction,
            self.Multitache
        ]
