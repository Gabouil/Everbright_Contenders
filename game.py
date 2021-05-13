from menu import *
from selectPlayer import *
from player1 import *
from player2 import *
from crowds import *


class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'BLKCHCRY.ttf'
        self.background = pygame.image.load("assets/game/bg.png")

        self.carte_use = None
        self.turn = 1
        self.turn2 = "Tourn 2"
        self.round = 1
        self.round2 = "Round 2 "

        #import de game dans les class
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.regles = Rule_menu(self)
        self.player1 = Player1(self)
        self.p1_maine_carte = Main_carte_p1(self)
        self.p2_maine_carte = Main_carte_p2(self)
        self.player2 = Player2(self)
        self.list_crowd = Liste_crowd(self)
        self.player_turn = self.player1
        self.player_not_turn = self.player2

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

        self.round2x, self.round2y = self.mid_w + 10, self.mid_h - 450 
        self.turn2x, self.turn2y = self.mid_w + 10, self.mid_h - 400
        
        self.button_carte_pl1x, self.button_carte_pl1y = self.mid_w - 360, self.mid_h + 250
        self.button_carte_pl2x, self.button_carte_pl2y = self.mid_w + 360, self.mid_h + 250

        self.button_exclamation_pl1x, self.button_exlamation_pl1y = self.mid_w - 520, self.mid_h + 300
        self.button_exclamation_pl2x, self.button_exlamation_pl2y = self.mid_w + 520, self.mid_h + 300

        self.button_victoire1_pl1x, self.button_victoire1_pl1y = self.mid_w - 399, self.mid_h - 405
        self.button_victoire2_pl1x, self.button_victoire2_pl1y = self.mid_w - 464, self.mid_h - 405
        
        self.button_victoire1_pl2x, self.button_victoire1_pl2y = self.mid_w + 399, self.mid_h - 405
        self.button_victoire2_pl2x, self.button_victoire2_pl2y = self.mid_w + 464, self.mid_h - 405

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

    def update_screen(self):
        self.window.blit(self.display, (0, 0))
        pygame.display.update()

    def init_game(self):
        self.player1.main_cartes()
        self.player2.main_cartes()
        self.player1.charge_sprit()
        self.player2.charge_sprit()
        self.list_crowd.charge_crowd()


    def init_manche(self):
        pass

    def game_loop(self):
        self.playing = True
        self.select_player_confirme = False
        self.init_game()
        print(self.player_turn.jauge_de_confiance)
        print(self.player_not_turn.jauge_de_confiance)
        while self.playing:
            self.check_events()
            self.display.blit(self.background, (0, 0))
            self.draw_text(self.player1.caractere.firstname + " " + self.player1.caractere.name, 40, (0,0,0), self.name_player1x, self.name_player1y)
            self.draw_text(self.player2.caractere.firstname + " " + self.player2.caractere.name, 40, (0,0,0), self.name_player2x, self.name_player2y)
            self.draw_text(' " '+self.player1.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player1x, self.surnom_player1y)
            self.draw_text(' " '+self.player2.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player2x, self.surnom_player2y)
            self.draw_text(self.round2, 50, (0,0,0), self.round2x, self.round2y)
            self.draw_text(self.turn2, 30, (0,128,0), self.turn2x, self.turn2y)
            self.display.blit(self.button_carte_pl1, self.button_carte_pl1_rect)
            self.display.blit(self.button_carte_pl2, self.button_carte_pl2_rect)
            self.display.blit(self.player1.sprit_player1, self.player1.sprit_player1_rect)
            self.display.blit(self.player2.sprit_player2, self.player2.sprit_player2_rect)
            self.display.blit(self.list_crowd.button_crowd, self.list_crowd.button_crowd_rect)
            self.display.blit(self.opion_button, self.opion_button_rect)
            self.display.blit(self.button_exlamation_pl1, self.button_exlamation_pl1_rect)
            self.display.blit(self.button_exlamation_pl2, self.button_exlamation_pl2_rect)
            self.display.blit(self.button_victoire1_pl1, self.button_victoire1_pl1_rect)
            self.display.blit(self.button_victoire2_pl1, self.button_victoire2_pl1_rect)
            self.display.blit(self.button_victoire1_pl2, self.button_victoire1_pl2_rect)
            self.display.blit(self.button_victoire2_pl2, self.button_victoire2_pl2_rect)
            
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
                # Button du jeux
                if self.curr_menu == Game:
                    if self.player_turn == self.player1:
                        if self.button_carte_pl1_rect.collidepoint(pygame.mouse.get_pos()):
                            self.curr_menu = self.p1_maine_carte
                            self.curr_menu.display_menu()

                    if self.player_turn == self.player2:
                        if self.button_carte_pl2_rect.collidepoint(pygame.mouse.get_pos()):
                            self.curr_menu = self.p2_maine_carte
                            self.curr_menu.display_menu()

                #bouton menu cartes
                if self.curr_menu == self.p1_maine_carte:
                    if self.p1_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.p1_maine_carte.no_option = False
                        self.curr_menu = Game
                    #click sur les carte
                    if self.button_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte1"
                        self.player1.carte1.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    if self.button_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte2"
                        self.player1.carte2.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    if self.button_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte3"
                        self.player1.carte3.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game

                if self.curr_menu == self.p2_maine_carte:
                    if self.p2_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    #click sur les carte
                    if self.button_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte1"
                        self.player2.carte1.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    if self.button_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte2"
                        self.player2.carte2.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
                        self.curr_menu = Game
                    if self.button_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                        self.carte_use = "carte3"
                        self.player2.carte3.effect_carte()
                        self.curr_menu.run_display = False
                        self.p2_maine_carte.no_option = False
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
                        if self.select_player.liam_select == False and self.select_player.player2 == False:
                            self.select_player.carte_liam = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.liam_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Liam(self, "Liam", "mcWarren", "populaire", "jeune", "M", "Le mercenaire")
                                self.select_player.player1 = "Liam"
                            else:
                                self.player2.caractere = Liam(self, "Liam", "mcWarren", "populaire", "jeune", "M", "Le mercenaire")
                                self.select_player.player2 = "Liam"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_ambre_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.ambre_select == False and self.select_player.player2 == False:
                            self.select_player.carte_ambre = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.ambre_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Ambre(self, "Ambre", "de Croy", "noble", "jeune", "F", "La demoiselle")
                                self.select_player.player1 = "Ambre"
                                
                            else:
                                self.player2.caractere = Ambre(self, "Ambre", "deCroy", "noble", "jeune", "F", "La demoiselle" )
                                self.select_player.player2 = "Ambre"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_alfred_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.alfred_select == False and self.select_player.player2 == False:
                            self.select_player.carte_alfred = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.alfred_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Alfred(self, "Alfred", "Heimsworth", "noble", "vieux", "M", "Le majordome")
                                self.select_player.player1 = "Alfred"
                            else:
                                self.player2.caractere = Alfred(self, "Alfred", "Heimsworth", "noble", "vieux", "M", "Le majordome")
                                self.select_player.player2 = "Alfred"
                        
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_crystal_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.crystal_select == False and self.select_player.player2 == False:
                            self.select_player.carte_crystal = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.crystal_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Crystal(self, "Crystal", "Devereux", "populaire", "vieux", "F", "Le requin")
                                self.select_player.player1 = "Crystal"

                            else:
                                self.player2.caractere = Crystal(self, "Crystal", "Devereux", "populaire", "vieux", "F", "Le requin")
                                self.select_player.player2 = "Crystal"


                    #menu règles
                if self.curr_menu == self.regles:
                    if self.regles.page != 1:
                        if self.regles.left_button_rect.collidepoint(pygame.mouse.get_pos()):
                            print("click gauche")
                            self.regles.page -= 1
                    if self.regles.page != 5:
                        if self.regles.right_button_rect.collidepoint(pygame.mouse.get_pos()):
                            print("click droite")
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




    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    class Liste_carte():
        def __init__(self,game):
            self.game = game
            # Liam
            self.True_story = True_story(self.game, "True story", "Unique")
            self.Peche_davarice = Peche_davarice(self.game, "Peche davarice", "Unique")
            self.Gamin_des_rues = Gamin_des_rues(self.game, "Gamin des rues", "Unique")
            # Ambre
            self.Secret_familial = Secret_familial(self.game, "Secret familial", "Unique")
            self.Regard_enjoleur = Regard_enjoleur(self.game, "Regard enjoleur", "Unique")
            self.Conseils_avisees = Conseils_avisees(self.game, "Conseils avisees", "Unique")
            # Alfred
            self.Cest_pas_au_vieux_singe = Cest_pas_au_vieux_singe(self.game, "Cest pas au vieux singe", "Unique")
            self.Seconde_vie = Seconde_vie(self.game, "Seconde vie", "Unique")
            self.Service_sur_mesure = Service_sur_mesure(self.game, "Service sur mesure", "Unique")
            # Crystal
            self.Rhetorique_de_limperatrice = Rhetorique_de_limperatrice(self.game, "Rhetorique de limperatrice", "Unique")
            self.Sombre_formule = Sombre_formule(self.game, "Sombre formule", "Unique")
            self.Influence_mystique = Influence_mystique(self.game, "Influence mystique", "Unique")
            # Cartes Comune
            # Jeune
            self.Gout_du_risque = Gout_du_risque(self.game, "Gout du risque", "Jeune")
            self.Sante_de_fer = Sante_de_fer(self.game, "Sante de fer", "Jeune")
            self.Adaptation = Adaptation(self.game, "Adaptation ", "Jeune")
            self.Esprit_vif = Esprit_vif(self.game, "Esprit vif ", "Jeune")
            # âgé
            self.Experience_de_lage = Experience_de_lage(self.game, "Experience de lage ", "âgé")
            self.Veteran = Veteran(self.game, " Veteran ", "âgé")
            self.Sante_fragile = Sante_fragile(self.game, " Sante fragile ", "âgé")
            self.Oeil_sage = Oeil_sage(self.game, " Oeil sage", "âgé")
            # Homme
            self.Avantage_masculin = Avantage_masculin(self.game, "Avantage masculin", "Homme")
            self.Tonalite_virile = Tonalite_virile(self.game, "Tonalite virile", "Homme")
            self.Sens_du_sacrifice = Sens_du_sacrifice(self.game, "Sens du sacrifice", "Homme")
            self.Monotache = Monotache(self.game, "Monotache", "Homme")
            # Femme
            self.Avantage_feminin = Avantage_feminin(self.game, "Avantage feminin", "Femme")
            self.Mauvaise_foi = Mauvaise_foi(self.game, "Mauvaise foi", "Femme")
            self.Seduction = Seduction(self.game, "Seduction", "Femme")
            self.Multitache = Multitache(self.game, "Multitache", "Femme")
            # Noble
            self.Opulence = Opulence(self.game, "Opulence", "Noble")
            self.Hautes_relations = Hautes_relations(self.game, "Hautes relations", "Noble")
            self.Mepris_du_fortune = Mepris_du_fortune(self.game, "Mepris du fortune", "Noble")
            self.Pot_de_vin = Pot_de_vin(self.game, "Pot de vin", "Noble")
            # Populaire
            self.Solidarite = Solidarite(self.game, "Solidarite", "Populaire")
            self.Priere_misericordieuse = Priere_misericordieuse(self.game, "Priere misericordieuse", "Populaire")
            self.Coup_de_chance = Coup_de_chance(self.game, "Coup de chance", "Populaire")
            self.Avantage_du_nombre = Avantage_du_nombre(self.game, "Avantage du nombre", "Populaire")