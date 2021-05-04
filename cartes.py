import random

class Cartes :
    def __init__(self, name, type):
        self.name = name
        self.type = type


class EXODIO(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)
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
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Peche_davarice(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Gamin_des_rues(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Ambre
class Secret_familial(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Regard_enjoleur(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Intimidation_par_procuration(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Alfred
class Cest_pas_au_vieux_singe(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Seconde_vie(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Service_sur_mesure(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Crystal
class Rhetorique_de_limperatrice(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Sombre_formule(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Influence_mystique(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Cartes Comune
#Jeune
class Gout_du_risque(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Sante_de_fer(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Adaptation(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Esprit_vif(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#âgé
class Experience_de_lage(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Veteran(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Sante_fragile(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Oeil_sage(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Homme
class Privilege_masculin(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Tonalite_virile(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Sens_du_sacrifice(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Monotache(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Femme
class Privilege_feminin(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Mauvaise_foi(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Seduction(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Multitache(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Noble
class Opulence(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Hautes_relations(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Mepris_du_fortune(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Pot_de_vin(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

#Populaire
class Solidarite(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Priere_misericordieuse(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Coup_de_chance(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass

class Avantage_du_nombre(Cartes):
    def __init__(self, name, type):
        Cartes.__init__(self, name, type)

    def effect_carte(self):
        pass
