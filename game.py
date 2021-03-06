from mots import *
from cartes import *
from menu import *
from selectPlayer import *
from player1 import *
from player2 import *
from crowds import *
from intro import *
from sound import *
from game_mots import *
from calcul_points import *

class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'BLKCHCRY.ttf'
        self.font_name_titre = 'Breathe.otf'
        self.background = pygame.image.load("assets/game/bg.png")

        self.carte_use = None
        self.liam_avarice = False
        self.turn = 1
        self.round = 1

        #import de game dans les class
        self.intro = Intro(self)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.regles = Rule_menu(self)
        self.about = About_menu(self)
        self.player1 = Player1(self)
        self.p1_maine_carte = Main_carte_p1(self)
        self.p2_maine_carte = Main_carte_p2(self)
        self.player2 = Player2(self)
        self.list_crowd = Liste_crowd(self)
        self.player_turn = self.player1
        self.player_not_turn = self.player2
        self.game_mots = Game_mots(self)
        self.calcul_points = Calcul_points(self)
        self.minimum_mot = 4

        self.liam = Liam(self, "Liam", "mcWarren", "populaire", "jeune", "M", "Le mercenaire")
        self.ambre = Ambre(self, "Ambre", "de Croy", "noble", "jeune", "F", "La demoiselle")
        self.alfred = Alfred(self, "Alfred", "Heimsworth", "noble", "vieux", "M", "Le majordome")
        self.crystal = Crystal(self, "Crystal", "Devereux", "populaire", "vieux", "F", "Le requin")

        #import de game dans la class selctplayer
        self.select_player = SelectPlayer(self)
        self.select_player_confirme = False

        self.curr_menu = self.main_menu

        #position des images
        self.optionx, self.optiony = self.DISPLAY_W - 80, self.DISPLAY_H - 60
        
        self.name_player1x, self.name_player1y = self.mid_w - 520, self.mid_h - 460
        self.name_player2x, self.name_player2y = self.mid_w + 520, self.mid_h - 460
        
        self.surnom_player1x, self.surnom_player1y = self.mid_w - 590, self.mid_h - 400
        self.surnom_player2x, self.surnom_player2y = self.mid_w + 590, self.mid_h - 400

        self.round2x, self.round2y = self.mid_w, self.mid_h - 460
        self.turn2x, self.turn2y = self.mid_w, self.mid_h - 410
        self.confience_p1x, self.confience_p1y = self.mid_w - 570, self.mid_h + 192
        self.confience_p2x, self.confience_p2y = self.mid_w + 565, self.mid_h + 192
        self.confience_barre_p1x, self.confience_barre_p1y = self.mid_w - 693, self.mid_h + 179
        self.confience_barre_p2x, self.confience_barre_p2y = self.mid_w + 584, self.mid_h + 179

        self.button_carte_pl1x, self.button_carte_pl1y = self.mid_w - 360, self.mid_h + 230
        self.button_carte_pl2x, self.button_carte_pl2y = self.mid_w + 360, self.mid_h + 230

        self.button_exclamation_pl1x, self.button_exlamation_pl1y = self.mid_w - 480, self.mid_h + 280
        self.button_exclamation_pl2x, self.button_exlamation_pl2y = self.mid_w + 475, self.mid_h + 280

        self.button_victoire1_pl1x, self.button_victoire1_pl1y = self.mid_w - 464, self.mid_h - 405
        self.button_victoire2_pl1x, self.button_victoire2_pl1y = self.mid_w - 399, self.mid_h - 405
        
        self.button_victoire1_pl2x, self.button_victoire1_pl2y = self.mid_w + 464, self.mid_h - 405
        self.button_victoire2_pl2x, self.button_victoire2_pl2y = self.mid_w + 399, self.mid_h - 405


        self.phrase_p1x, self.phrase_p1y = self.mid_w, self.mid_h + 336
        self.phrase_p2x, self.phrase_p2y = self.mid_w, self.mid_h + 386

        self.crowdx, self.crowdy = self.mid_w, self.mid_h + 220
        #Bouton du jeux
        self.button_carte_pl1 = pygame.image.load("assets/game/bouton_menu_carte.png")
        self.button_carte_pl1_rect = self.button_carte_pl1.get_rect()
        self.button_carte_pl1_rect.center = (self.button_carte_pl1x, self.button_carte_pl1y)
        
        self.button_carte_pl2 = pygame.image.load("assets/game/bouton_menu_carte.png")
        self.button_carte_pl2_rect = self.button_carte_pl1.get_rect()
        self.button_carte_pl2_rect.center = (self.button_carte_pl2x, self.button_carte_pl2y)

        self.button_exlamation_pl1 = pygame.image.load("assets/game/exclamation.png")
        self.button_exlamation_pl1_rect = self.button_exlamation_pl1.get_rect()
        self.button_exlamation_pl1_rect.center = (self.button_exclamation_pl1x, self.button_exlamation_pl1y) 
        
        self.button_exlamation_pl2 = pygame.image.load("assets/game/exclamation.png")
        self.button_exlamation_pl2_rect = self.button_exlamation_pl2.get_rect()
        self.button_exlamation_pl2_rect.center = (self.button_exclamation_pl2x, self.button_exlamation_pl2y)

        self.button_victoire1_pl1 = pygame.image.load("assets/game/check_win.png")
        self.button_victoire1_pl1_rect = self.button_victoire1_pl1.get_rect()
        self.button_victoire1_pl1_rect.center = (self.button_victoire1_pl1x, self.button_victoire1_pl1y) 
        self.button_victoire2_pl1 = pygame.image.load("assets/game/check_win.png")
        self.button_victoire2_pl1_rect = self.button_victoire2_pl1.get_rect()
        self.button_victoire2_pl1_rect.center = (self.button_victoire2_pl1x, self.button_victoire2_pl1y) 
        
        self.button_victoire1_pl2 = pygame.image.load("assets/game/check_win.png")
        self.button_victoire1_pl2_rect = self.button_victoire1_pl2.get_rect()
        self.button_victoire1_pl2_rect.center = (self.button_victoire1_pl2x, self.button_victoire1_pl2y) 
        self.button_victoire2_pl2 = pygame.image.load("assets/game/check_win.png")
        self.button_victoire2_pl2_rect = self.button_victoire2_pl2.get_rect()
        self.button_victoire2_pl2_rect.center = (self.button_victoire2_pl2x, self.button_victoire2_pl2y) 


        #bouton des options
        self.opion_button = pygame.image.load("assets/option_button.png")
        self.opion_button_rect = self.opion_button.get_rect()
        self.opion_button_rect.center = (self.optionx, self.optiony)
    
    def update_phrase(self):
        self.player_turn.phrase = ""
        for mot in self.player_turn.mots:
            self.player_turn.phrase += mot.name + " "
        self.player_not_turn.phrase = ""
        for mot in self.player_not_turn.mots:
            self.player_not_turn.phrase += mot.name + " "
        
    def end_turn(self):
        self.turn += 1
        if self.player_turn.carte_oblige:
            if self.player_turn.carte_oblige_conteur == 0:
                self.player_turn.carte_oblige_conteur += 1
            elif self.player_turn.carte_oblige_conteur == 1:
                self.player_turn.carte_oblige_conteur = 0
                self.player_turn.carte_oblige = False
        if self.player_turn.antie_vol:
            self.player_turn.antie_vol_conteur += 1
            if self.player_turn.antie_vol_conteur >= 3:
                self.player_turn.antie_vol_conteur = 0
                self.player_turn.antie_vol = False
        if self.player_turn.liam_avarice:
            self.player_turn.liam_avarice_conteur += 1
            self.player_turn.jauge_de_confiance += 5
            if self.player_turn.liam_avarice_conteur >= 5:
                self.player_turn.liam_avarice = False
                self.player_turn.liam_avarice_conteur = 0
        player_turn = self.player_turn
        player_not_turn = self.player_not_turn
        self.player_turn = player_not_turn
        self.player_not_turn = player_turn
        self.update_screen()

    def update_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def init_game(self):
        self.player1.main_cartes()
        self.player2.main_cartes()
        self.player1.charge_sprit()
        self.player2.charge_sprit()
        self.player1.exodio.retour_du_dieu()
        self.list_crowd.charge_crowd()
        self.game_mots.select_mots()
        self.game_mots.charge_mots()


    def init_manche(self):
        if self.player1.carte1 == None:
            self.player1.number_carte1 = randint(0, 14)
            while self.player1.number_carte1 == self.player1.number_carte2 or self.player1.number_carte1 == self.player1.number_carte3:
                self.player1.number_carte1 = randint(0, 14)
            self.player1.carte1 = self.player1.caractere.list_cartes[self.player1.number_carte1]
        if self.player1.carte2 == None:
            self.player1.number_carte2 = randint(0, 14)
            while self.player1.number_carte2 == self.player1.number_carte1 or self.player1.number_carte2 == self.player1.number_carte3:
                self.player1.number_carte2 = randint(0, 14)
            self.player1.carte2 = self.player1.caractere.list_cartes[self.player1.number_carte2]
        if self.player1.carte3 == None:
            self.player1.number_carte3 = randint(0, 14)
            while self.player1.number_carte3 == self.player1.number_carte1 or self.player1.number_carte3 == self.player1.number_carte2:
                self.player1.number_carte3 = randint(0, 14)
            self.player1.carte3 = self.player1.caractere.list_cartes[self.player1.number_carte3]
        if self.player2.carte1 == None:
            self.player2.number_carte1 = randint(0, 14)
            while self.player2.number_carte1 == self.player1.number_carte2 or self.player2.number_carte1 == self.player1.number_carte3:
                self.player2.number_carte1 = randint(0, 14)
            self.player2.carte1 = self.player2.caractere.list_cartes[self.player2.number_carte1]
        if self.player2.carte2 == None:
            self.player2.number_carte2 = randint(0, 14)
            while self.player2.number_carte2 == self.player1.number_carte1 or self.player2.number_carte2 == self.player1.number_carte3:
                self.player2.number_carte2 = randint(0, 14)
            self.player2.carte2 = self.player2.caractere.list_cartes[self.player2.number_carte2]
        if self.player2.carte3 == None:
            self.player2.number_carte3 = randint(0, 14)
            while self.player2.number_carte3 == self.player1.number_carte2 or self.player2.number_carte3 == self.player1.number_carte1:
                self.player2.number_carte3 = randint(0, 14)
            self.player2.carte3 = self.player2.caractere.list_cartes[self.player2.number_carte3]
        self.player1.phrase = ""
        self.player1.mots = []
        self.player2.phrase = ""
        self.player2.mots = []

        self.game_mots.liste_mots.groupe_nominaux = [
            self.game_mots.liste_mots.votre_apparence,
            self.game_mots.liste_mots.votre_prose,
            self.game_mots.liste_mots.rien_que_vous_ecouter_jouter,
            self.game_mots.liste_mots.voyou_a_la_petite_semaine,
            self.game_mots.liste_mots.votre_talent,
            self.game_mots.liste_mots.certains,
            self.game_mots.liste_mots.une_lice,
            self.game_mots.liste_mots.affronter_une_gamine,
            self.game_mots.liste_mots.ton_style,
            self.game_mots.liste_mots.pour_toi,
            self.game_mots.liste_mots.ton_manque_dexperience,
            self.game_mots.liste_mots.perroquet_frippe,
            self.game_mots.liste_mots.la_tension,
            self.game_mots.liste_mots.oh_petite_precieuse,
            self.game_mots.liste_mots.petit_servant,
            self.game_mots.liste_mots.faquin,
            self.game_mots.liste_mots.hypocrite,
            self.game_mots.liste_mots.fripouille,
            self.game_mots.liste_mots.paltoquet,
            self.game_mots.liste_mots.prostitue_en_mailles,
            self.game_mots.liste_mots.diable,
            self.game_mots.liste_mots.chez_tes_parents,
            self.game_mots.liste_mots.votre_odeur,
            self.game_mots.liste_mots.petit_minable,
            self.game_mots.liste_mots.quel_rate,
            self.game_mots.liste_mots.les_bottes_de_ton_maitre,
            self.game_mots.liste_mots.ta_place,
            self.game_mots.liste_mots.ton_visage,
            self.game_mots.liste_mots.pimbeche,
            self.game_mots.liste_mots.cuistre,
            self.game_mots.liste_mots.maraud,
            self.game_mots.liste_mots.gourgandine,
            self.game_mots.liste_mots.eunuque,
            self.game_mots.liste_mots.pourceau,
            self.game_mots.liste_mots.jeune_ignorant,
            self.game_mots.liste_mots.vieille_peau
        ]

        self.game_mots.liste_mots.complements = [
            self.game_mots.liste_mots.petit_servant,
            self.game_mots.liste_mots.faquin,
            self.game_mots.liste_mots.hypocrite,
            self.game_mots.liste_mots.fripouille,
            self.game_mots.liste_mots.paltoquet,
            self.game_mots.liste_mots.prostitue_en_mailles,
            self.game_mots.liste_mots.diable,
            self.game_mots.liste_mots.chez_tes_parents,
            self.game_mots.liste_mots.votre_odeur,
            self.game_mots.liste_mots.petit_minable,
            self.game_mots.liste_mots.quel_rate,
            self.game_mots.liste_mots.les_bottes_de_ton_maitre,
            self.game_mots.liste_mots.ta_place,
            self.game_mots.liste_mots.ton_visage,
            self.game_mots.liste_mots.pimbeche,
            self.game_mots.liste_mots.cuistre,
            self.game_mots.liste_mots.maraud,
            self.game_mots.liste_mots.gourgandine,
            self.game_mots.liste_mots.eunuque,
            self.game_mots.liste_mots.pourceau,
            self.game_mots.liste_mots.jeune_ignorant,
            self.game_mots.liste_mots.vieille_peau,
            self.game_mots.liste_mots.retournez_dans_votre_bouge,
            self.game_mots.liste_mots.laisse_moi_rire,
            self.game_mots.liste_mots.allons_donc,
            self.game_mots.liste_mots.de_vos_magouilles,
            self.game_mots.liste_mots.vu_de_pres,
            self.game_mots.liste_mots.apparemment,
            self.game_mots.liste_mots.ce_matin,
            self.game_mots.liste_mots.cest_ca_le_theme,
            self.game_mots.liste_mots.cest_ca_que_taimes,
            self.game_mots.liste_mots.ben_voyons,
            self.game_mots.liste_mots.si_on_ta_promis_la_gloire,
            self.game_mots.liste_mots.pour_sur,
            self.game_mots.liste_mots.est_dans_un_musee,
            self.game_mots.liste_mots.on_ta_menti,
            self.game_mots.liste_mots.nest_pas_tres_joli_a_voir,
            self.game_mots.liste_mots.ce_que_tu_cherches,
            self.game_mots.liste_mots.sale_vaurien

        ]

        self.game_mots.liste_mots.groupe_verbaux = [
            self.game_mots.liste_mots.est_dans_un_musee,
            self.game_mots.liste_mots.on_ta_menti,
            self.game_mots.liste_mots.nest_pas_tres_joli_a_voir,
            self.game_mots.liste_mots.ce_que_tu_cherches,
            self.game_mots.liste_mots.sale_vaurien,
            self.game_mots.liste_mots.est_si_famelique,
            self.game_mots.liste_mots.est_minable,
            self.game_mots.liste_mots.vous_etes_vous_relu,
            self.game_mots.liste_mots.parlez_nous,
            self.game_mots.liste_mots.rentre,
            self.game_mots.liste_mots.as_lair_si_bete,
            self.game_mots.liste_mots.na_rien_a_envier,
            self.game_mots.liste_mots.est_tombe_dans_le_crottin,
            self.game_mots.liste_mots.est_palpable,
            self.game_mots.liste_mots.tes_courgeux,
            self.game_mots.liste_mots.a_plus_de_rides_que_toi,
            self.game_mots.liste_mots.va_ten_lecher,
            self.game_mots.liste_mots.on_se_demande_bien,
            self.game_mots.liste_mots.tu_sors_de_ton_ecrin

        ]
        self.game_mots.liste_mots.conjonction_de_coordination = [
            self.game_mots.liste_mots.mais,
            self.game_mots.liste_mots.ou,
            self.game_mots.liste_mots.et,
            self.game_mots.liste_mots.donc,
            self.game_mots.liste_mots.or_,
            self.game_mots.liste_mots.ni,
            self.game_mots.liste_mots.car
        ]

        self.player1.antie_critique = False
        self.player2.antie_critique = False
        self.list_crowd.change_crowd = True
        self.round += 1



    def max_mot(self):
        if len(self.player1.mots) == 8:
            self.calcul_points.calcul_points()
            self.calcul_points.who_win()
        if len(self.player2.mots) == 8:
            self.calcul_points.calcul_points()
            self.calcul_points.who_win()

    def game_loop(self):
        self.playing = True
        self.select_player_confirme = False
        self.init_game()
        quel_battel = random.randint(1,2)
        pygame.mixer.music.load("song/battel"+ str(quel_battel) +".mp3")
        pygame.mixer.music.play(0)
        while self.playing:
            # print(self.player_turn.jauge_de_confiance)
            self.display.blit(self.background, (0, 0))
            self.draw_text(self.player1.caractere.firstname + " " + self.player1.caractere.name, 40, (0,0,0), self.name_player1x, self.name_player1y, self.font_name)
            self.draw_text(self.player2.caractere.firstname + " " + self.player2.caractere.name, 40, (0,0,0), self.name_player2x, self.name_player2y, self.font_name)
            self.draw_text(' " '+self.player1.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player1x, self.surnom_player1y, self.font_name)
            self.draw_text(' " '+self.player2.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player2x, self.surnom_player2y, self.font_name)
            self.draw_text("round " + str(self.round), 50, (0,0,0), self.round2x, self.round2y, self.font_name_titre)
            self.draw_text('Tour du joueur ' + str(self.player_turn.player), 30, (0,128,0), self.turn2x, self.turn2y, self.font_name)
            pygame.draw.rect(self.display, (0,250,0), pygame.Rect(self.confience_barre_p1x, self.confience_barre_p1y, 100 + self.player1.jauge_de_confiance, 29))
            pygame.draw.rect(self.display, (0,250,0), pygame.Rect(self.confience_barre_p2x - self.player2.jauge_de_confiance, self.confience_barre_p2y, 100 + self.player2.jauge_de_confiance, 29))
            if self.player1.jauge_de_confiance >= 0:
                self.draw_text(str(self.player1.jauge_de_confiance), 30, (0,0,250), self.confience_p1x, self.confience_p1y, self.font_name)
            else:
                self.draw_text(str(self.player1.jauge_de_confiance), 30, (250,0,0), self.confience_p1x, self.confience_p1y, self.font_name)
            if self.player2.jauge_de_confiance >= 0:
                self.draw_text(str(self.player2.jauge_de_confiance), 30, (0,0,250), self.confience_p2x, self.confience_p2y, self.font_name)
            else:
                self.draw_text(str(self.player2.jauge_de_confiance), 30, (250,0,0), self.confience_p2x, self.confience_p2y, self.font_name)
            self.display.blit(self.button_carte_pl1, self.button_carte_pl1_rect)
            self.display.blit(self.button_carte_pl2, self.button_carte_pl2_rect)
            self.display.blit(self.player1.sprit_player1, self.player1.sprit_player1_rect)
            self.display.blit(self.player2.sprit_player2, self.player2.sprit_player2_rect)
            self.display.blit(self.list_crowd.button_crowd, self.list_crowd.button_crowd_rect)
            self.display.blit(self.button_exlamation_pl1, self.button_exlamation_pl1_rect)
            self.display.blit(self.button_exlamation_pl2, self.button_exlamation_pl2_rect)
            if self.player1.win1:
                self.display.blit(self.button_victoire1_pl1, self.button_victoire1_pl1_rect)
            if self.player2.win1:
                self.display.blit(self.button_victoire1_pl2, self.button_victoire1_pl2_rect)
            #print mots
            self.display.blit(self.game_mots.button_mot1, self.game_mots.button_mot1_rect)
            if self.game_mots.efficace1:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot1_rect)
            if self.game_mots.pas_efficace1:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot1_rect)
            self.display.blit(self.game_mots.button_mot2, self.game_mots.button_mot2_rect)
            if self.game_mots.efficace2:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot2_rect)
            if self.game_mots.pas_efficace2:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot2_rect)
            self.display.blit(self.game_mots.button_mot3, self.game_mots.button_mot3_rect)
            if self.game_mots.efficace3:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot3_rect)
            if self.game_mots.pas_efficace3:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot3_rect)
            self.display.blit(self.game_mots.button_mot4, self.game_mots.button_mot4_rect)
            if self.game_mots.efficace4:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot4_rect)
            if self.game_mots.pas_efficace4:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot4_rect)
            self.display.blit(self.game_mots.button_mot5, self.game_mots.button_mot5_rect)
            if self.game_mots.efficace5:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot5_rect)
            if self.game_mots.pas_efficace5:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot5_rect)
            self.display.blit(self.game_mots.button_mot6, self.game_mots.button_mot6_rect)
            if self.game_mots.efficace6:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot6_rect)
            if self.game_mots.pas_efficace6:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot6_rect)
            self.display.blit(self.game_mots.button_mot7, self.game_mots.button_mot7_rect)
            if self.game_mots.efficace7:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot7_rect)
            if self.game_mots.pas_efficace7:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot7_rect)
            self.display.blit(self.game_mots.button_mot8, self.game_mots.button_mot8_rect)
            if self.game_mots.efficace8:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot8_rect)
            if self.game_mots.pas_efficace8:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot8_rect)
            self.display.blit(self.game_mots.button_mot9, self.game_mots.button_mot9_rect)
            if self.game_mots.efficace9:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot9_rect)
            if self.game_mots.pas_efficace9:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot9_rect)
            self.display.blit(self.game_mots.button_mot10, self.game_mots.button_mot10_rect)
            if self.game_mots.efficace10:
                self.display.blit(self.game_mots.efficace_img, self.game_mots.button_mot10_rect)
            if self.game_mots.pas_efficace10:
                self.display.blit(self.game_mots.pas_efficace_img, self.game_mots.button_mot10_rect)

            self.draw_text(self.player1.phrase, 20, (0, 0, 0), self.phrase_p1x, self.phrase_p1y,self.font_name)
            self.draw_text(self.player2.phrase, 20, (0, 0, 0), self.phrase_p2x, self.phrase_p2y,self.font_name)
            self.max_mot()
            self.check_events()
            self.display.blit(self.opion_button, self.opion_button_rect)

            self.update_screen()

    def charge_carte_p1(self):
        if self.player1.carte1 == None:
            self.button_carte1 = self.p1_maine_carte.carte_none
        else:
            self.button_carte1 = self.player1.carte1.img
        self.button_carte1_rect = self.button_carte1.get_rect()
        self.button_carte1_rect.center = (self.player1.pcarte1x, self.player1.pcarte1y)

        if self.player1.carte2 == None:
            self.button_carte2 = self.p1_maine_carte.carte_none
        else:
            self.button_carte2 = self.player1.carte2.img
        self.button_carte2_rect = self.button_carte2.get_rect()
        self.button_carte2_rect.center = (self.player1.pcarte2x, self.player1.pcarte2y)

        if self.player1.carte3 == None:
            self.button_carte3 = self.p1_maine_carte.carte_none
        else:
            self.button_carte3 = self.player1.carte3.img
        self.button_carte3_rect = self.button_carte3.get_rect()
        self.button_carte3_rect.center = (self.player1.pcarte3x, self.player1.pcarte3y)

    def charge_carte_p2(self):
        if self.player2.carte1 == None:
            self.button_carte1 = self.p2_maine_carte.carte_none
        else:
            self.button_carte1 = self.player2.carte1.img
        self.button_carte1_rect = self.button_carte1.get_rect()
        self.button_carte1_rect.center = (self.player2.pcarte1x, self.player2.pcarte1y)

        if self.player2.carte2 == None:
            self.button_carte2 = self.p2_maine_carte.carte_none
        else:
            self.button_carte2 = self.player2.carte2.img
        self.button_carte2_rect = self.button_carte2.get_rect()
        self.button_carte2_rect.center = (self.player2.pcarte2x, self.player2.pcarte2y)

        if self.player2.carte3 == None:
            self.button_carte3 = self.p2_maine_carte.carte_none
        else:
            self.button_carte3 = self.player2.carte3.img
        self.button_carte3_rect = self.button_carte3.get_rect()
        self.button_carte3_rect.center = (self.player2.pcarte3x, self.player2.pcarte3y)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                # Button du jeux
                if self.curr_menu == Game:
                    if self.player_turn == self.player1:
                        if self.button_carte_pl1_rect.collidepoint(pygame.mouse.get_pos()):
                            self.curr_menu = self.p1_maine_carte
                            self.curr_menu.display_menu()
                        if len(self.player1.mots) >= self.minimum_mot:
                            if self.button_exlamation_pl1_rect.collidepoint(pygame.mouse.get_pos()):
                                self.calcul_points.calcul_points()
                                self.calcul_points.who_win()
                                self.update_screen()
                    if self.player_turn == self.player2:
                        if self.button_carte_pl2_rect.collidepoint(pygame.mouse.get_pos()):
                            self.curr_menu = self.p2_maine_carte
                            self.curr_menu.display_menu()
                        if len(self.player2.mots) >= self.minimum_mot:
                            if self.button_exlamation_pl2_rect.collidepoint(pygame.mouse.get_pos()):
                                self.calcul_points.calcul_points()
                                self.calcul_points.who_win()
                                self.update_screen()

                    if self.player_turn.carte_oblige == False:
                        if self.game_mots.button_mot1_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace1:
                                self.game_mots.efficace1 = False
                            if self.game_mots.pas_efficace1:
                                self.game_mots.pas_efficace1 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot1)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot1 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot1 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot1]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot1]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot1)
                                self.update_phrase()
                                self.game_mots.choix_mot2 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot1 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot1]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot1]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot2_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace2:
                                self.game_mots.efficace2 = False
                            if self.game_mots.pas_efficace2:
                                self.game_mots.pas_efficace2 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot2)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot2 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot2 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot2]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot2]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot2)
                                self.update_phrase()
                                self.game_mots.choix_mot2 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot2 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot2]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot2]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot3_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace3:
                                self.game_mots.efficace3 = False
                            if self.game_mots.pas_efficace3:
                                self.game_mots.pas_efficace3 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot3)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot3 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot3 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot3]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot3]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot3)
                                self.update_phrase()
                                self.game_mots.choix_mot3 = random.randint(0, len(self.game_mots.liste_mots.groupe_nominaux)-1)
                                self.game_mots.mot3 = self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot3]
                                del self.game_mots.liste_mots.groupe_nominaux[self.game_mots.choix_mot3]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot4_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace4:
                                self.game_mots.efficace4 = False
                            if self.game_mots.pas_efficace4:
                                self.game_mots.pas_efficace4 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot4)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot4 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot4 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot4]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot4]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot4)
                                self.update_phrase()
                                self.game_mots.choix_mot4 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot4 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot4]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot4]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot5_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace5:
                                self.game_mots.efficace5 = False
                            if self.game_mots.pas_efficace5:
                                self.game_mots.pas_efficace5 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot5)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot5 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot5 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot5]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot5]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot5)
                                self.update_phrase()
                                self.game_mots.choix_mot5 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot5 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot5]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot5]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot6_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace6:
                                self.game_mots.efficace6 = False
                            if self.game_mots.pas_efficace6:
                                self.game_mots.pas_efficace6 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot6)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot6 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot6 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot6]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot6]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot6)
                                self.update_phrase()
                                self.game_mots.choix_mot6 = random.randint(0, len(self.game_mots.liste_mots.complements)-1)
                                self.game_mots.mot6 = self.game_mots.liste_mots.complements[self.game_mots.choix_mot6]
                                del self.game_mots.liste_mots.complements[self.game_mots.choix_mot6]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot7_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace7:
                                self.game_mots.efficace7 = False
                            if self.game_mots.pas_efficace7:
                                self.game_mots.pas_efficace7 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot7)
                                self.update_phrase() 
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot7 = random.randint(0, len(self.game_mots.liste_mots.groupe_verbaux)-1)
                                self.game_mots.mot7 = self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot7]
                                del self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot7]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot7)
                                self.update_phrase()
                                self.game_mots.choix_mot7 = random.randint(0, len(self.game_mots.liste_mots.groupe_verbaux)-1)
                                self.game_mots.mot7 = self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot7]
                                del self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot7]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot8_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace8:
                                self.game_mots.efficace8 = False
                            if self.game_mots.pas_efficace8:
                                self.game_mots.pas_efficace8 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot8)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot8 = random.randint(0, len(self.game_mots.liste_mots.groupe_verbaux)-1)
                                self.game_mots.mot8 = self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot8]
                                del self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot8]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot8)
                                self.update_phrase()
                                self.game_mots.choix_mot8 = random.randint(0, len(self.game_mots.liste_mots.groupe_verbaux)-1)
                                self.game_mots.mot8 = self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot8]
                                del self.game_mots.liste_mots.groupe_verbaux[self.game_mots.choix_mot8]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot9_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace9:
                                self.game_mots.efficace9 = False
                            if self.game_mots.pas_efficace9:
                                self.game_mots.pas_efficace9 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot9)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot9 = random.randint(0, len(self.game_mots.liste_mots.conjonction_de_coordination)-1)
                                self.game_mots.mot9 = self.game_mots.liste_mots.conjonction_de_coordination[self.game_mots.choix_mot9]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot9)
                                self.update_phrase()
                                self.game_mots.choix_mot9 = random.randint(0, len(self.game_mots.liste_mots.conjonction_de_coordination)-1)
                                self.game_mots.mot9 = self.game_mots.liste_mots.conjonction_de_coordination[self.game_mots.choix_mot9]
                                self.game_mots.charge_mots()
                                self.end_turn()
                        if self.game_mots.button_mot10_rect.collidepoint(pygame.mouse.get_pos()):
                            if self.game_mots.efficace10:
                                self.game_mots.efficace10 = False
                            if self.game_mots.pas_efficace10:
                                self.game_mots.pas_efficace10 = False
                            if self.player_turn.mot_free:
                                self.player_turn.mots.append(self.game_mots.mot10)
                                self.update_phrase()
                                self.player_turn.mot_free = False
                                self.game_mots.choix_mot10 = random.randint(0, len(self.game_mots.liste_mots.conjonction_de_coordination)-1)
                                self.game_mots.mot10 = self.game_mots.liste_mots.conjonction_de_coordination[self.game_mots.choix_mot10]
                                self.game_mots.charge_mots()
                            else:
                                self.player_turn.mots.append(self.game_mots.mot10)
                                self.update_phrase()
                                self.game_mots.choix_mot10 = random.randint(0, len(self.game_mots.liste_mots.conjonction_de_coordination)-1)
                                self.game_mots.mot10 = self.game_mots.liste_mots.conjonction_de_coordination[self.game_mots.choix_mot10]
                                self.game_mots.charge_mots()
                                self.end_turn()

                #bouton menu cartes
                if self.curr_menu == self.p1_maine_carte:
                    if self.p1_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.p1_maine_carte.no_option = False
                        self.curr_menu = Game
                    #click sur les carte
                    if self.player1.carte1 != None:
                        if self.button_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte1"
                            self.curr_menu.run_display = False
                            self.p1_maine_carte.no_option = False
                            self.player1.carte1.effect_carte()
                            self.curr_menu = Game
                    if self.player1.carte2 != None:
                        if self.button_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte2"
                            self.curr_menu.run_display = False
                            self.p1_maine_carte.no_option = False
                            self.player1.carte2.effect_carte()
                            self.curr_menu = Game
                    if self.player1.carte3 != None:
                        if self.button_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte3"
                            self.curr_menu.run_display = False
                            self.p1_maine_carte.no_option = False
                            self.player1.carte3.effect_carte()
                            self.curr_menu = Game

                if self.curr_menu == self.p2_maine_carte:
                    if self.p2_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    #click sur les carte
                    if self.player2.carte1 != None:
                        if self.button_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte1"
                            self.curr_menu.run_display = False
                            self.p2_maine_carte.no_option = False
                            self.player2.carte1.effect_carte()
                            self.curr_menu = Game
                    if self.player2.carte2 != None:
                        if self.button_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte2"
                            self.curr_menu.run_display = False
                            self.p2_maine_carte.no_option = False
                            self.player2.carte2.effect_carte()
                            self.curr_menu = Game
                    if self.player2.carte3 != None:
                        if self.button_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                            click_carte.play()
                            self.carte_use = "carte3"
                            self.curr_menu.run_display = False
                            self.p2_maine_carte.no_option = False
                            self.player2.carte3.effect_carte()
                            self.curr_menu = Game



                # Button main menu

                if self.p1_maine_carte.no_option == False and self.p2_maine_carte.no_option == False:
                    if self.main_menu.opion_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.options
                        self.curr_menu.display_menu()
                if self.curr_menu == self.main_menu:
                    if self.main_menu.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.select_player
                        self.curr_menu.display_menu()
                    if self.main_menu.rules_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.regles
                        self.curr_menu.display_menu()
                    if self.main_menu.about_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.about
                        self.curr_menu.display_menu()
                    if self.main_menu.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.running, self.playing = False, False
                        self.curr_menu.run_display = False
                        pygame.quit()



                # button option

                if self.curr_menu == self.options:
                    if self.options.songM_rect.collidepoint(pygame.mouse.get_pos()):
                        self.options.song_niv -= 0.1
                        if self.options.song_niv <= 0.1:
                            self.options.song_niv = 0.1
                        pygame.mixer.music.set_volume(self.options.song_niv)
                        self.options.song = pygame.image.load("assets/song_" + str(int(self.options.song_niv * 10)) + ".png")
                    if self.options.songP_rect.collidepoint(pygame.mouse.get_pos()):
                        self.options.song_niv += 0.1
                        if self.options.song_niv >= 1:
                            self.options.song_niv = 1
                        pygame.mixer.music.set_volume(self.options.song_niv)
                        self.options.song = pygame.image.load("assets/song_" + str(int(self.options.song_niv * 10)) + ".png")
                    if self.options.song_check_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.options.song_check_checked:
                            self.options.song_check_checked = False
                        else:
                            self.options.song_check_checked = True
                    if self.options.soundM_rect.collidepoint(pygame.mouse.get_pos()):
                        self.options.sound_niv -= 0.1
                        if self.options.sound_niv <= 0.1:
                            self.options.sound_niv = 0.1
                        pygame.mixer.music.set_volume(self.options.sound_niv)
                        self.options.sound = pygame.image.load("assets/song_" + str(int(self.options.sound_niv * 10)) + ".png")
                    if self.options.soundP_rect.collidepoint(pygame.mouse.get_pos()):
                        self.options.sound_niv += 0.1
                        if self.options.sound_niv >= 1:
                            self.options.sound_niv = 1
                        pygame.mixer.music.set_volume(self.options.sound_niv)
                        self.options.sound = pygame.image.load("assets/song_" + str(int(self.options.sound_niv * 10)) + ".png")
                    if self.options.sound_check_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.options.sound_check_checked:
                            self.options.sound_check_checked = False
                        else:
                            self.options.sound_check_checked = True

                    if self.options.rules_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.regles
                        self.curr_menu.display_menu()
                    if self.options.close_option_rect.collidepoint(pygame.mouse.get_pos()):
                        self.options.option = False
                        if self.select_player_confirme:
                            self.curr_menu.run_display = False
                            self.curr_menu = self.select_player
                        elif self.playing:
                            self.curr_menu.run_display = False
                            self.curr_menu = Game
                        else:
                            self.curr_menu.run_display = False
                            self.curr_menu = self.main_menu



                    # Button selection player
                if self.curr_menu == self.select_player:
                    if self.select_player.button_start_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = Game
                        self.select_player.run_display = False
                        self.curr_menu.game_loop(self)
                    if self.select_player.carte_liam_rect.collidepoint(pygame.mouse.get_pos()):
                        click_carte.play()
                        if self.select_player.liam_select == False and self.select_player.player2 == False:
                            self.select_player.carte_liam = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.liam_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = self.liam
                                self.select_player.player1 = "Liam"
                            else:
                                self.player2.caractere = self.liam
                                self.select_player.player2 = "Liam"
                    if self.select_player.carte_ambre_rect.collidepoint(pygame.mouse.get_pos()):
                        click_carte.play()
                        if self.select_player.ambre_select == False and self.select_player.player2 == False:
                            self.select_player.carte_ambre = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.ambre_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = self.ambre
                                self.select_player.player1 = "Ambre"
                                
                            else:
                                self.player2.caractere = self.ambre
                                self.select_player.player2 = "Ambre"
                    if self.select_player.carte_alfred_rect.collidepoint(pygame.mouse.get_pos()):
                        click_carte.play()
                        if self.select_player.alfred_select == False and self.select_player.player2 == False:
                            self.select_player.carte_alfred = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.alfred_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = self.alfred
                                self.select_player.player1 = "Alfred"
                            else:
                                self.player2.caractere = self.alfred
                                self.select_player.player2 = "Alfred"

                    if self.select_player.carte_crystal_rect.collidepoint(pygame.mouse.get_pos()):
                        click_carte.play()
                        if self.select_player.crystal_select == False and self.select_player.player2 == False:
                            self.select_player.carte_crystal = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.crystal_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = self.crystal
                                self.select_player.player1 = "Crystal"

                            else:
                                self.player2.caractere = self.crystal
                                self.select_player.player2 = "Crystal"


                    #menu r??gles
                if self.curr_menu == self.regles:
                    if self.regles.page != 1:
                        if self.regles.left_button_rect.collidepoint(pygame.mouse.get_pos()):
                            self.regles.page -= 1
                    if self.regles.page != 5:
                        if self.regles.right_button_rect.collidepoint(pygame.mouse.get_pos()):
                            self.regles.page += 1
                    if self.regles.close_option_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player_confirme:
                            self.curr_menu.run_display = False
                            self.curr_menu = self.select_player
                            self.curr_menu.display_menu()
                        elif self.playing:
                            self.curr_menu.run_display = False
                            self.curr_menu = Game
                            self.curr_menu.game_loop(self)
                        else:
                            self.curr_menu.run_display = False
                            self.curr_menu = self.main_menu
                            self.curr_menu.display_menu()

                # menu About
                if self.curr_menu == self.about:
                    if self.about.page != 1:
                        if self.about.left_button_rect.collidepoint(pygame.mouse.get_pos()):
                            self.about.page -= 1
                    if self.about.page != 5:
                        if self.about.right_button_rect.collidepoint(pygame.mouse.get_pos()):
                            self.about.page += 1
                    if self.about.close_option_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.curr_menu = self.main_menu
                        self.curr_menu.display_menu()

                #menu de fin
                if self.calcul_points.win != None:
                    if self.calcul_points.button_menu_rect.collidepoint(pygame.mouse.get_pos()):
                        # self.curr_menu.run_display = False
                        # self.curr_menu = self.main_menu
                        # self.player1 = Player1(self)
                        # self.player2 = Player2(self)
                        # self.curr_menu.display_menu()
                        self.running, self.playing = False, False
                        self.curr_menu.run_display = False
                        pygame.quit()




    def draw_text(self, text, size, color, x, y, font_charge):
        font = pygame.font.Font(font_charge,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)





    class Liste_carte():
        def __init__(self,game):
            self.game = game
            # Liam
            self.True_story = True_story(self.game, "True story", "Argent")
            self.Peche_davarice = Peche_davarice(self.game, "Peche davarice", "Bronze")
            self.Gamin_des_rues = Gamin_des_rues(self.game, "Gamin des rues", "Bronze")
            # Ambre
            self.Secret_familial = Secret_familial(self.game, "Secret familial", "Argent")
            self.Regard_enjoleur = Regard_enjoleur(self.game, "Regard enjoleur", "Bronze")
            self.Conseils_avisees = Conseils_avisees(self.game, "Conseils avisees", "Bronze")
            # Alfred
            self.Cest_pas_au_vieux_singe = Cest_pas_au_vieux_singe(self.game, "Cest pas au vieux singe", "Argent")
            self.Seconde_vie = Seconde_vie(self.game, "Seconde vie", "Bronze")
            self.Service_sur_mesure = Service_sur_mesure(self.game, "Service sur mesure", "Bronze")
            # Crystal
            self.Rhetorique_de_limperatrice = Rhetorique_de_limperatrice(self.game, "Rhetorique de limperatrice", "Argent")
            self.Sombre_formule = Sombre_formule(self.game, "Sombre formule", "Bronze")
            self.Influence_mystique = Influence_mystique(self.game, "Influence mystique", "Bronze")
            # Cartes Comune
            # Jeune
            self.Gout_du_risque = Gout_du_risque(self.game, "Gout du risque", "Acier")
            self.Sante_de_fer = Sante_de_fer(self.game, "Sante de fer", "Acier")
            self.Adaptation = Adaptation(self.game, "Adaptation ", "Acier")
            self.Esprit_vif = Esprit_vif(self.game, "Esprit vif ", "Acier")
            # ??g??
            self.Experience_de_lage = Experience_de_lage(self.game, "Experience de lage ", "Acier")
            self.Veteran = Veteran(self.game, " Veteran ", "Acier")
            self.Sante_fragile = Sante_fragile(self.game, " Sante fragile ", "Acier")
            self.Oeil_sage = Oeil_sage(self.game, " Oeil sage", "Acier")
            # Homme
            self.Avantage_masculin = Avantage_masculin(self.game, "Avantage masculin", "Acier")
            self.Tonalite_virile = Tonalite_virile(self.game, "Tonalite virile", "Acier")
            self.Sens_du_sacrifice = Sens_du_sacrifice(self.game, "Sens du sacrifice", "Acier")
            self.Monotache = Monotache(self.game, "Monotache", "Acier")
            # Femme
            self.Avantage_feminin = Avantage_feminin(self.game, "Avantage feminin", "Acier")
            self.Mauvaise_foi = Mauvaise_foi(self.game, "Mauvaise foi", "Acier")
            self.Seduction = Seduction(self.game, "Seduction", "Acier")
            self.Multitache = Multitache(self.game, "Multitache", "Acier")
            # Noble
            self.Opulence = Opulence(self.game, "Opulence", "Noble")
            self.Hautes_relations = Hautes_relations(self.game, "Hautes relations", "Acier")
            self.Mepris_du_fortune = Mepris_du_fortune(self.game, "Mepris du fortune", "Acier")
            self.Pot_de_vin = Pot_de_vin(self.game, "Pot de vin", "Acier")
            # Populaire
            self.Solidarite = Solidarite(self.game, "Solidarite", "Acier")
            self.Priere_misericordieuse = Priere_misericordieuse(self.game, "Priere misericordieuse", "Acier")
            self.Coup_de_chance = Coup_de_chance(self.game, "Coup de chance", "Acier")
            self.Avantage_du_nombre = Avantage_du_nombre(self.game, "Avantage du nombre", "Acier")

    class Liste_mot():
        def __init__(self,game):
            self.game = game
            #Groupe nominaux
            self.votre_apparence = votre_apparence(self.game,"votre apparence", "Groupe nominaux")
            self.votre_prose = votre_prose(self.game, "votre prose", "Groupe nominaux")
            self.rien_que_vous_ecouter_jouter = rien_que_vous_ecouter_jouter(self.game, "rien que vous ??couter jouter","Groupe nominaux")
            self.voyou_a_la_petite_semaine = voyou_a_la_petite_semaine(self.game, "voyou ?? la petite semaine", "Groupe nominaux")
            self.votre_talent = votre_talent(self.game, "votre talent", "Groupe nominaux")
            self.certains = certains(self.game, "certains", "Groupe nominaux")
            self.une_lice = une_lice(self.game, "une lice", "Groupe nominaux")
            self.affronter_une_gamine = affronter_une_gamine(self.game, "affronter une gamine", "Groupe nominaux")
            self.ton_style = ton_style(self.game, "ton style", "Groupe nominaux")
            self.pour_toi = pour_toi(self.game, "pour toi", "Groupe nominaux")
            self.ton_manque_dexperience = ton_manque_dexperience(self.game, "ton manque d'exp??rience", "Groupe nominaux")
            self.perroquet_frippe = perroquet_frippe(self.game, "perroquet frippe", "Groupe nominaux")
            self.la_tension = la_tension(self.game, "la tension", "Groupe nominaux")
            self.oh_petite_precieuse = oh_petite_precieuse(self.game, "oh petite precieuse", "Groupe nominaux")
            #Groupes Nominaux / complements
            self.petit_servant = petit_servant(self.game, "petit servant", "Groupes Nominaux / complements")
            self.faquin = faquin(self.game, "faquin", "Groupes Nominaux / complements")
            self.hypocrite = hypocrite(self.game, "hypocrite", "Groupes Nominaux / complements")
            self.fripouille = fripouille(self.game, "fripouille", "Groupes Nominaux / complements")
            self.paltoquet = paltoquet(self.game, "paltoquet", "Groupes Nominaux / complements")
            self.prostitue_en_mailles = prostitue_en_mailles(self.game, "prostitue_en_mailles", "Groupes Nominaux / complements")
            self.diable = diable(self.game, "diable", "Groupes Nominaux / complements")
            self.chez_tes_parents = chez_tes_parents(self.game, "chez tes parents", "Groupes Nominaux / complements")
            self.votre_odeur = votre_odeur(self.game, "votre odeur", "Groupes Nominaux / complements")
            self.petit_minable = petit_minable(self.game, "petit minable", "Groupes Nominaux / complements")
            self.quel_rate = quel_rate(self.game, "quel rat??", "Groupes Nominaux / complements")
            self.les_bottes_de_ton_maitre = les_bottes_de_ton_maitre(self.game, "les_bottes_de_ton_maitre", "Groupes Nominaux / complements")
            self.ta_place = ta_place(self.game, "ta place", "Groupes Nominaux / complements")
            self.ton_visage = ton_visage(self.game, "ton visage", "Groupes Nominaux / complements")
            self.pimbeche = pimbeche(self.game, "pimb??che", "Groupes Nominaux / complements")
            self.cuistre = cuistre(self.game, "cuistre", "Groupes Nominaux / complements")
            self.maraud = maraud(self.game, "maraud", "Groupes Nominaux / complements")
            self.gourgandine = gourgandine(self.game, "gourgandine", "Groupes Nominaux / complements")
            self.eunuque = eunuque(self.game, "eunuque", "Groupes Nominaux / complements")
            self.pourceau = pourceau(self.game, "pourceau", "Groupes Nominaux / complements")
            self.jeune_ignorant = jeune_ignorant(self.game, "jeune ignorant", "Groupes Nominaux / complements")
            self.vieille_peau = vieille_peau(self.game, "vieille peau", "Groupes Nominaux / complements")
            #Compl??ments
            self.retournez_dans_votre_bouge = retournez_dans_votre_bouge(self.game, "retournez dans votre bouge", "complements")
            self.laisse_moi_rire = laisse_moi_rire(self.game, "laisse moi rire", "complements")
            self.allons_donc = allons_donc(self.game, "allons donc", "complements")
            self.de_vos_magouilles = de_vos_magouilles(self.game, "de vos magouilles", "complements")
            self.vu_de_pres = vu_de_pres(self.game, "vu de pr??s", "complements")
            self.apparemment = apparemment(self.game, "apparemment", "complements")
            self.ce_matin = ce_matin(self.game, "ce matin", "complements")
            self.cest_ca_le_theme = cest_ca_le_theme(self.game, "c'est ??a le th??me", "complements")
            self.cest_ca_que_taimes = cest_ca_que_taimes(self.game, "c'est ??a que t'aimes", "complements")
            self.ben_voyons = ben_voyons(self.game, "ben voyons", "complements")
            self.si_on_ta_promis_la_gloire = si_on_ta_promis_la_gloire(self.game, "si on t'a promis la gloire", "complements")
            self.pour_sur = pour_sur(self.game, "pour s??r", "complements")
            #Groupes verbaux / compl??ments
            self.est_dans_un_musee = est_dans_un_musee(self.game, "est dans un mus??e", "Groupes verbaux / compl??ments")
            self.on_ta_menti = on_ta_menti(self.game, "on t'a menti", "Groupes verbaux / compl??ments")
            self.nest_pas_tres_joli_a_voir = nest_pas_tres_joli_a_voir(self.game, "n'est pas tr??s joli ?? voir", "Groupes verbaux / compl??ments")
            self.ce_que_tu_cherches = ce_que_tu_cherches(self.game, "ce que tu cherches", "Groupes verbaux / compl??ments")
            self.sale_vaurien = sale_vaurien(self.game, "sale vaurien", "Groupes verbaux / compl??ments")
            #Groupes verbaux
            self.est_si_famelique = est_si_famelique(self.game, "est si famelique", "Groupes verbaux")
            self.est_minable = est_minable(self.game, "est minable", "Groupes verbaux")
            self.vous_etes_vous_relu = vous_etes_vous_relu(self.game, "vous etes-vous relu", "Groupes verbaux")
            self.parlez_nous = parlez_nous(self.game, "parlez nous", "Groupes verbaux")
            self.rentre = rentre(self.game, "rentre", "Groupes verbaux")
            self.as_lair_si_bete = as_lair_si_bete(self.game, "as l'air si b??te", "Groupes verbaux")
            self.na_rien_a_envier = na_rien_a_envier(self.game, "na rien a envier", "Groupes verbaux")
            self.est_tombe_dans_le_crottin = est_tombe_dans_le_crottin(self.game, "est tombe dans le crottin", "Groupes verbaux")
            self.est_palpable = est_palpable(self.game, "est palpable", "Groupes verbaux")
            self.tes_courgeux = tes_courgeux(self.game, "t'es courgeux", "Groupes verbaux")
            self.a_plus_de_rides_que_toi = a_plus_de_rides_que_toi(self.game, "a plus de rides que toi", "Groupes verbaux")
            self.va_ten_lecher = va_ten_lecher(self.game, "va t'en lecher", "Groupes verbaux")
            self.on_se_demande_bien = on_se_demande_bien(self.game, "on se demande bien", "Groupes verbaux")
            self.tu_sors_de_ton_ecrin = tu_sors_de_ton_ecrin(self.game, "tu sors de ton ecrin", "Groupes verbaux")
            #Conjoction de coordination
            self.mais = mais(self.game, "mais", "Conjoction de coordination")
            self.ou = ou(self.game, "ou", "Conjoction de coordination")
            self.et = et(self.game, "et", "Conjoction de coordination")
            self.donc = donc(self.game, "donc", "Conjoction de coordination")
            self.or_ = or_(self.game, "or", "Conjoction de coordination")
            self.ni = ni(self.game, "ni", "Conjoction de coordination")
            self.car = car(self.game, "car", "Conjoction de coordination")


            self.groupe_nominaux = [
                self.votre_apparence,
                self.votre_prose,
                self.rien_que_vous_ecouter_jouter,
                self.voyou_a_la_petite_semaine,
                self.votre_talent,
                self.certains,
                self.une_lice,
                self.affronter_une_gamine,
                self.ton_style,
                self.pour_toi,
                self.ton_manque_dexperience,
                self.perroquet_frippe,
                self.la_tension,
                self.oh_petite_precieuse,
                self.petit_servant,
                self.faquin,
                self.hypocrite,
                self.fripouille,
                self.paltoquet,
                self.prostitue_en_mailles,
                self.diable,
                self.chez_tes_parents,
                self.votre_odeur,
                self.petit_minable,
                self.quel_rate,
                self.les_bottes_de_ton_maitre,
                self.ta_place,
                self.ton_visage,
                self.pimbeche,
                self.cuistre,
                self.maraud,
                self.gourgandine,
                self.eunuque,
                self.pourceau,
                self.jeune_ignorant,
                self.vieille_peau
            ]

            self.complements = [
                self.petit_servant,
                self.faquin,
                self.hypocrite,
                self.fripouille,
                self.paltoquet,
                self.prostitue_en_mailles,
                self.diable,
                self.chez_tes_parents,
                self.votre_odeur,
                self.petit_minable,
                self.quel_rate,
                self.les_bottes_de_ton_maitre,
                self.ta_place,
                self.ton_visage,
                self.pimbeche,
                self.cuistre,
                self.maraud,
                self.gourgandine,
                self.eunuque,
                self.pourceau,
                self.jeune_ignorant,
                self.vieille_peau,
                self.retournez_dans_votre_bouge,
                self.laisse_moi_rire,
                self.allons_donc,
                self.de_vos_magouilles,
                self.vu_de_pres,
                self.apparemment,
                self.ce_matin,
                self.cest_ca_le_theme,
                self.cest_ca_que_taimes,
                self.ben_voyons,
                self.si_on_ta_promis_la_gloire,
                self.pour_sur,
                self.est_dans_un_musee,
                self.on_ta_menti,
                self.nest_pas_tres_joli_a_voir,
                self.ce_que_tu_cherches,
                self.sale_vaurien

            ]

            self.groupe_verbaux = [
                self.est_dans_un_musee,
                self.on_ta_menti,
                self.nest_pas_tres_joli_a_voir,
                self.ce_que_tu_cherches,
                self.sale_vaurien,
                self.est_si_famelique,
                self.est_minable,
                self.vous_etes_vous_relu,
                self.parlez_nous,
                self.rentre,
                self.as_lair_si_bete,
                self.na_rien_a_envier,
                self.est_tombe_dans_le_crottin,
                self.est_palpable,
                self.tes_courgeux,
                self.a_plus_de_rides_que_toi,
                self.va_ten_lecher,
                self.on_se_demande_bien,
                self.tu_sors_de_ton_ecrin

            ]
            self.conjonction_de_coordination = [
                self.mais,
                self.ou,
                self.et,
                self.donc,
                self.or_,
                self.ni,
                self.car
            ]



