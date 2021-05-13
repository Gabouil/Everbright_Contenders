import pygame
class Mots :
    def __init__(self, game,  name, type ):
        self.game = game
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.motx, self.moty = self.mid_w, self.mid_h


#-------------Groupe nominaux---------------------------------------

class votre_apparence:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/votre_apparence.png")

class votre_prose:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/votre_prose.png")

class rien_que_vous_ecouter_jouter:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/rien_que_de_vous_ecouter_jouter.png")

class voyou_a_la_petite_semaine:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/voyou_a_la_petite_semaine.png")      
class votre_talent:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/votre_talent.png")

class certains:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/certains.png")

class une_lice:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/une_lice.png")
        

class affronter_une_gamine:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/affronter_une_gamine.png")
        
class ton_style:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ton_style.png")

class pour_toi:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/pour_toi.png")
        
class ton_manque_dexperience:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ton_manque_dexperience.png")

class perroquet_frippe:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/perroquet_frippe.png")

class la_tension:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/la_tension.png")

class oh_petite_precieuse:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/oh_petite_precieuse.png")


#------------------Groupes Nominaux / complements--------------------------------
class petit_servant:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/petit_servant.png")
class faquin:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/faquin.png")
class hypocrite:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/hypocrite.png")
class fripouille:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/fripouille.png")

class paltoquet:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/paltoquet.png")

class prostitue_en_mailles:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/prostitue_en_mailles.png")

class diable:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/diable.png")

class chez_tes_parents:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/chez_tes_parents.png")

class votre_odeur:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/votre_odeur.png")

class petit_minable:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/petit_minable.png")

class quel_rate:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/quel_rate.png")

class les_bottes_de_ton_maitre:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/les_bottes_de_ton_maitre.png")

class ta_place:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ta_place.png")

class ton_visage:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ton_visage.png")

class pimbeche:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/pimbeche.png")

class cuistre:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/cuistre.png")

class maraud:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/maraud.png")

class gourgandine:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/gourgandine.png")

class eunuque:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/eunuque.png")

class pourceau:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/pourceau.png")

class jeune_ignorant:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/jeune_ignorant.png")

class vieille_peau:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/vieille_peau.png")


#--------------Compléments-------------------------------------------

class retournez_dans_votre_bouge:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/retournez_dans_votre_bouge.png")

class laisse_moi_rire:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/laisse_moi_rire.png")

class allons_donc:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/allons_donc.png")

class de_vos_magouilles:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/de_vos_magouilles.png")

class vu_de_pres:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/vu_de_pres.png")

class apparemment:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/apparemment.png")
        #ajouter image

class ce_matin:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ce_matin.png")

class cest_ca_le_theme:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/cest_ca_le_theme.png")

class cest_ca_que_taimes:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/cest_ca_que_taimes.png")

class ben_voyons:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ben_voyons.png")

class si_on_ta_promis_la_gloire:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/si_on_ta_promis_la_gloire.png")

class pour_sur:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/pour_sur.png")

#-------------------Groupes verbaux / compléments-----------------------------

class est_dans_un_musee:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/est_dans_un_musee.png")

class on_ta_menti:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/on_ta_menti.png")

class nest_pas_tres_joli_a_voir:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/nest_pas_tres_joli_a_voir.png")

class ce_que_tu_cherches:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ce_que_tu_cherches.png")

class sale_vaurien:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/sale_vaurien.png")

#---------------Groupes verbaux---------------------------------------------

class est_si_famelique:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/est_si_famelique.png")

class est_minable:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/est_minable.png")

class vous_etes_vous_relu:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/vous_etes_vous_relu.png")

class parlez_nous:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/parlez_nous.png")

class rentre:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/rentre.png")

class as_lair_si_bete:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/as_lair_si_bete.png")

class na_rien_a_envier:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/na_rien_a_envier.png")

class est_tombe_dans_le_crottin:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/est_tombe_dans_le_crottin.png")

class est_palpable:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/est_palpable.png")

class tes_courgeux:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/tes_courgeux.png")

class a_plus_de_rides_que_toi:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/a_plus_de_rides_que_toi.png")

class va_ten_lecher:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/va_ten_lecher.png")

class on_se_demande_bien:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/on_se_demande_bien.png")

class tu_sors_de_ton_ecrin:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/tu_sors_de_ton_ecrin.png")

#-----Conjoction de coordination---------------
class mais:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/mais.png")

class ou:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ou.png")

class et:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/et.png")

class donc:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/donc.png")

class or_:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/or.png")

class ni:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/ni.png")

class car:
    def __init__(self, game,  name, type):
        Mots.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/mots/car.png")


