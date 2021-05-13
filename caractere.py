from cartes import *
from mots import *
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
        self.list_mot_efficace = []
        self.list_mot_tres_efficace = []
        self.list_mot_neutre = []
        self.list_mot_inneficace = []
        
        

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
        self.cartes = self.game.Liste_carte(game)
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
        self.mots = self.game.Liste_mot(game)
        self.list_mot_efficace = [
            self.mots.ton_manque_dexperience,
            self.mots.petit_minable,
            self.mots.maraud,
            self.mots.eunuque,
            self.mots.pourceau,
            self.mots.jeune_ignorant,
            self.mots.retournez_dans_votre_bouge,
            self.mots.sale_vaurien,
            self.mots.est_si_famelique,
            self.mots.tu_sors_de_ton_ecrin, 
            
            ]
        self.list_mot_tres_efficace = [
            self.mots.voyou_a_la_petite_semaine,
            self.mots.prostitue_en_mailles,
            self.mots.votre_odeur,
        ]
        self.list_mot_neutre = [
            self.mots.rien_que_vous_ecouter_jouter,
            self.mots.certains,
            self.mots.lice,
            self.mots.ton_style, 
            self.mots.pour_toi,
            self.mots.la_tension,
            self.mots.faquin,
            self.mots.fripouille,
            self.mots.diable,
            self.mots.quel_rate,
            self.mots.les_bottes_de_ton_maitre,
            self.mots.ta_place,
            self.mots.ton_visage,
            self.mots.laisse_moi_rire,
            self.mots.allons_donc, 
            self.mots.de_vos_magouillesself.apparemment,
            self.mots.ce_matin,
            self.mots.cest_ca_le_theme,
            self.mots.cest_ca_que_taimes ,
            self.mots.ben_voyons, 
            self.mots.si_on_ta_promis_la_gloire,
            self.mots.pour_sur,
            self.mots.on_ta_menti, 
            self.mots.nest_pas_tres_joli_a_voir,
            self.mots.ce_que_tu_cherches,
            self.mots.est_minable, 
            self.mots.vous_etes_vous_relu, 
            self.mots.parlez_nous,
            self.mots.rentre, 
            self.mots.as_lair_si_bete, 
            self.mots.na_rien_a_envier, 
            self.mots.est_tombe_dans_le_crottin, 
            self.mots.est_palpable, 
            self.mots.tes_courgeux, 
            #selfmots..a_plus_de_rides_que_toi  à voir
            self.mots.va_ten_lecher, 
            self.mots.on_se_demande_bien,
            self.mots.mais ,
            self.mots.ou ,
            self.mots.et ,
            self.mots.donc ,
            self.mots.or_,
            self.mots.ni,
            self.mots.car,  
        ]
        self.list_mot_inneficace = [
            self.mots.votre_apparence,
            self.mots.votre_prose,
            self.mots.affronter_une_gamine,
            self.mots.perroquet_frippe,
            self.mots.oh_petite_precieuse,
            self.mots.paltoquet,
            self.mots.pimbeche,
            self.mots.cuistre,
            self.mots.gourgandine,
            self.mots.vieille_peau,
            self.mots.est_dans_un_musee,
        ]
class Ambre(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.img = pygame.image.load("assets/cartes/carte_ambre.png")
        self.cartes = self.game.Liste_carte(game)
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
        self.mots = self.game.Liste_mot(game)
        self.list_mot_efficace = [
            self.mots.ton_manque_dexperience,
            self.mots.oh_petite_precieuse,
            self.mots.paltoquet,
            self.mots.petit_minable,
            self.mots.pimbeche,
            self.mots.cuistre,
            self.mots.gourgandine,
            self.mots.jeune_ignorant,
        ]
        self.list_mot_tres_efficace = [
            self.mots.affronter_une_gamine,
            self.mots.hypocrite,
            self.mots.chez_tes_parents,
        ]
        self.list_mot_neutre = [
            self.mots.rien_que_vous_ecouter_jouter,
            self.mots.certains,
            self.mots.lice,
            self.mots.ton_style, 
            self.mots.pour_toi,
            self.mots.la_tension,
            self.mots.faquin,
            self.mots.fripouille,
            self.mots.diable,
            self.mots.quel_rate,
            self.mots.les_bottes_de_ton_maitre, 
            self.mots.ta_place,
            self.mots.ton_visage,
            self.mots.laisse_moi_rire,
            self.mots.allons_donc, 
            self.mots.de_vos_magouillesself.apparemment,
            self.mots.ce_matin,
            self.mots.cest_ca_le_theme,
            self.mots.cest_ca_que_taimes ,
            self.mots.ben_voyons, 
            self.mots.si_on_ta_promis_la_gloire,
            self.mots.pour_sur,
            self.mots.on_ta_menti, 
            self.mots.nest_pas_tres_joli_a_voir,
            self.mots.ce_que_tu_cherches,
            self.mots.est_minable, 
            self.mots.vous_etes_vous_relu, 
            self.mots.parlez_nous,
            self.mots.rentre, 
            self.mots.as_lair_si_bete, 
            self.mots.na_rien_a_envier, 
            self.mots.est_tombe_dans_le_crottin, 
            self.mots.est_palpable, 
            self.mots.tes_courgeux, 
            #selfmots..a_plus_de_rides_que_toi  à voir
            self.mots.va_ten_lecher, 
            self.mots.on_se_demande_bien,
            self.mots.mais ,
            self.mots.ou ,
            self.mots.et ,
            self.mots.donc ,
            self.mots.or_,
            self.mots.ni,
            self.mots.car,   
        ]
        self.list_mot_inneficace = [
            self.mots.votre_talent,
            self.mots.perroquet_frippe,
            self.mots.petit_servant,
            self.mots.maraud,
            self.mots.eunuque,
            self.mots.pourceau,
            self.mots.vieille_peau,
            self.mots.retournez_dans_votre_bouge,
            self.mots.est_dans_un_musee,
            self.mots.sale_vaurien,
            self.mots.est_si_famelique,
            self.mots.tu_sors_de_ton_ecrin,  
        ]
        
class Alfred(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.cartes = self.game.Liste_carte(game)
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
        self.mots = self.game.Liste_mot(game)
        self.list_mot_efficace = [
            self.mots.perroquet_frippe,
            self.mots.paltoquet,
            self.mots.cuistre,
            self.mots.maraud,
            self.mots.eunuque,
            self.mots.pourceau,
            self.mots.vieille_peau,
            self.mots.est_dans_un_musee,
        ]
        self.list_mot_tres_efficace = [
            self.mots.petit_servant,
            self.mots.faquin,
            self.mots.les_bottes_de_ton_maitre ,
            
        ]
        self.list_mot_neutre = [
            self.mots.rien_que_vous_ecouter_jouter,
            self.mots.certains,
            self.mots.lice,
            self.mots.ton_style, 
            self.mots.pour_toi,
            self.mots.la_tension,
            self.mots.fripouille,
            self.mots.diable,
            self.mots.ta_place,
            self.mots.ton_visage,
            self.mots.laisse_moi_rire,
            self.mots.allons_donc, 
            self.mots.de_vos_magouillesself.apparemment,
            self.mots.ce_matin,
            self.mots.cest_ca_le_theme,
            self.mots.cest_ca_que_taimes ,
            self.mots.ben_voyons, 
            self.mots.si_on_ta_promis_la_gloire,
            self.mots.pour_sur,
            self.mots.on_ta_menti, 
            self.mots.nest_pas_tres_joli_a_voir,
            self.mots.ce_que_tu_cherches,
            self.mots.est_minable, 
            self.mots.vous_etes_vous_relu, 
            self.mots.parlez_nous,
            self.mots.rentre, 
            self.mots.as_lair_si_bete, 
            self.mots.na_rien_a_envier, 
            self.mots.est_tombe_dans_le_crottin, 
            self.mots.est_palpable, 
            self.mots.tes_courgeux, 
            #selfmots..a_plus_de_rides_que_toi  à voir
            self.mots.va_ten_lecher, 
            self.mots.on_se_demande_bien,
            self.mots.mais ,
            self.mots.ou ,
            self.mots.et ,
            self.mots.donc ,
            self.mots.or_,
            self.mots.ni,
            self.mots.car,   
        ]
        self.list_mot_inneficace = [
            self.mots.voyou_a_la_petite_semaine,
            self.mots.oh_petite_precieuse,
            self.mots.hypocrite,
            self.mots.chez_tes_parents,
            self.mots.petit_minable,
            self.mots.quel_rate,
            self.mots.pimbeche,
            self.mots.gourgandine,
            self.mots.jeune_ignorant,
            self.mots.retournez_dans_votre_bouge,
            self.mots.sale_vaurien,
            self.mots.est_si_famelique,
            self.mots.tu_sors_de_ton_ecrin,  
        ]
        
class Crystal(Caractere):
    def __init__(self,game, firstname, name, classe_sociale, age, sexe, surnom):
        Caractere.__init__(self,game, firstname, name, classe_sociale, age, sexe, surnom)
        self.cartes = self.game.Liste_carte(game)
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
        self.mots = self.game.Liste_mot(game)
        self.list_mot_efficace = [
            self.mots.perroquet_frippe,
            self.mots.oh_petite_precieuse,
            self.mots.pimbeche,
            self.mots.gourgandine,
            self.mots.vieille_peau,
            self.mots.retournez_dans_votre_bouge,
            self.mots.est_dans_un_musee,
            self.mots.sale_vaurien,
            self.mots.est_si_famelique,
            self.mots.tu_sors_de_ton_ecrin,  
        ]
        self.list_mot_tres_efficace = [
            self.mots.votre_apparence,
            self.mots.votre_prose,
            self.mots.votre_talent


            ]
        self.list_mot_neutre = [
            self.mots.rien_que_vous_ecouter_jouter,
            self.mots.certains,
            self.mots.lice,
            self.mots.ton_style, 
            self.mots.pour_toi,
            self.mots.la_tension,
            self.mots.faquin,
            self.mots.fripouille,
            self.mots.diable,
            self.mots.quel_rate,
            self.mots.les_bottes_de_ton_maitre,
            self.mots.ta_place,
            self.mots.ton_visage,
            self.mots.laisse_moi_rire,
            self.mots.allons_donc, 
            self.mots.de_vos_magouillesself.apparemment,
            self.mots.ce_matin,
            self.mots.cest_ca_le_theme,
            self.mots.cest_ca_que_taimes ,
            self.mots.ben_voyons, 
            self.mots.si_on_ta_promis_la_gloire,
            self.mots.pour_sur,
            self.mots.on_ta_menti, 
            self.mots.nest_pas_tres_joli_a_voir,
            self.mots.ce_que_tu_cherches,
            self.mots.est_minable, 
            self.mots.vous_etes_vous_relu, 
            self.mots.parlez_nous,
            self.mots.rentre, 
            self.mots.as_lair_si_bete, 
            self.mots.na_rien_a_envier, 
            self.mots.est_tombe_dans_le_crottin, 
            self.mots.est_palpable, 
            self.mots.tes_courgeux, 
            #selfmots..a_plus_de_rides_que_toi  à voir
            self.mots.va_ten_lecher, 
            self.mots.on_se_demande_bien,
            self.mots.mais ,
            self.mots.ou ,
            self.mots.et ,
            self.mots.donc ,
            self.mots.or_,
            self.mots.ni,
            self.mots.car,    

            ]
        self.list_mot_inneficace = [
            self.mots.voyou_a_la_petite_semaine,
            self.mots.paltoquet,
            self.mots.prostitue_en_mailles,
            self.mots.votre_odeur,
            self.mots.petit_minable,
            self.mots.cuistre,
            self.mots.maraud,
            self.mots.eunuque,
            self.mots.pourceau,
            self.mots.jeune_ignorant,
            
        ]



