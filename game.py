from menu import *
from selectPlayer import *
from player1 import *
from player2 import *
#from crowds import *


class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'Seagram.ttf'
        self.background = pygame.image.load("assets/game/bg.png")
        

        #import de game dans les class menu
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)
        self.player1 = Player1(self)
        self.p1_maine_carte = Main_carte_p1(self)
        self.p2_maine_carte = Main_carte_p2(self)
        self.player2 = Player2(self)
        #self.list_crowd = []

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
        
        self.button_carte_pl1x, self.button_carte_pl1y = self.mid_w - 360, self.mid_h + 250
        self.button_carte_pl2x, self.button_carte_pl2y = self.mid_w + 360, self.mid_h + 250

        self.button_exclamation_pl1x, self.button_exlamation_pl1y = self.mid_w - 520, self.mid_h + 300
        self.button_exclamation_pl2x, self.button_exlamation_pl2y = self.mid_w + 520, self.mid_h + 300

        self.button_victoire1_pl1x, self.button_victoire1_pl1y = self.mid_w - 399, self.mid_h - 405
        self.button_victoire2_pl1x, self.button_victoire2_pl1y = self.mid_w - 464, self.mid_h - 405
        
        self.button_victoire1_pl2x, self.button_victoire1_pl2y = self.mid_w + 399, self.mid_h - 405
        self.button_victoire2_pl2x, self.button_victoire2_pl2y = self.mid_w + 464, self.mid_h - 405

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
        self.init_manche()
        self.player1.charge_sprit()
        self.player2.charge_sprit()

    def init_manche(self):
        self.player1.main_cartes()
        self.player2.main_cartes()

    def game_loop(self):
        self.playing = True
        self.init_game()
        while self.playing:
            self.check_events()
            self.display.blit(self.background, (0, 0))
            self.draw_text(self.player1.caractere.firstname + " " + self.player1.caractere.name, 40, (0,0,0), self.name_player1x, self.name_player1y)
            self.draw_text(self.player2.caractere.firstname + " " + self.player2.caractere.name, 40, (0,0,0), self.name_player2x, self.name_player2y)
            self.draw_text(' " '+self.player1.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player1x, self.surnom_player1y)
            self.draw_text(' " '+self.player2.caractere.surnom+' " ', 25, (0,0,0), self.surnom_player2x, self.surnom_player2y)
            self.display.blit(self.button_carte_pl1, self.button_carte_pl1_rect)
            self.display.blit(self.button_carte_pl2, self.button_carte_pl2_rect)
            self.display.blit(self.player1.sprit_player1, self.player1.sprit_player1_rect)
            self.display.blit(self.player2.sprit_player2, self.player2.sprit_player2_rect)
            self.display.blit(self.opion_button, self.opion_button_rect)
            self.display.blit(self.button_exlamation_pl1, self.button_exlamation_pl1_rect)
            self.display.blit(self.button_exlamation_pl2, self.button_exlamation_pl2_rect)
            self.display.blit(self.button_victoire1_pl1, self.button_victoire1_pl1_rect)
            self.display.blit(self.button_victoire2_pl1, self.button_victoire2_pl1_rect)
            self.display.blit(self.button_victoire1_pl2, self.button_victoire1_pl2_rect)
            self.display.blit(self.button_victoire2_pl2, self.button_victoire2_pl2_rect)
            
            self.update_screen()

    def charge_carte_p1(self):
        self.button_carte1 = self.player1.carte1.img
        self.button_carte1_rect = self.button_carte1.get_rect()
        self.button_carte1_rect.center = (self.player1.pcarte1x, self.player1.pcarte1y)

        self.button_carte2 = self.player1.carte2.img
        self.button_carte2_rect = self.button_carte2.get_rect()
        self.button_carte2_rect.center = (self.player1.pcarte2x, self.player1.pcarte2y)

        self.button_carte3 = self.player1.carte3.img
        self.button_carte3_rect = self.button_carte3.get_rect()
        self.button_carte3_rect.center = (self.player1.pcarte3x, self.player1.pcarte3y)
    
    def charge_carte_p2(self):
        self.button_carte1 = self.player2.carte1.img
        self.button_carte1_rect = self.button_carte1.get_rect()
        self.button_carte1_rect.center = (self.player2.pcarte1x, self.player2.pcarte1y)

        self.button_carte2 = self.player2.carte2.img
        self.button_carte2_rect = self.button_carte2.get_rect()
        self.button_carte2_rect.center = (self.player2.pcarte2x, self.player2.pcarte2y)

        self.button_carte3 = self.player2.carte3.img
        self.button_carte3_rect = self.button_carte3.get_rect()
        self.button_carte3_rect.center = (self.player2.pcarte3x, self.player2.pcarte3y)
    
    #def charge_crowd(self):
    #    self.button_crowd = self.crowd.img
    #    self.button_crowd_rect = self.button_crowd.get_rect()
    #    self.button_crowd_rect.center = (self.crowdx, self.crowdy)

    #def alea_crowd(self):
    #    self.number_crowd = randint(0, 5)
    #    self.carte1 = self.game.list_crowd[self.number_crowd]




    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Button du jeux
                if self.curr_menu == Game:
                    if self.button_carte_pl1_rect.collidepoint(pygame.mouse.get_pos()):
                        print(self.player1.carte1.img, self.player1.carte1.name)
                        self.curr_menu = self.p1_maine_carte
                        self.curr_menu.display_menu()

                    if self.button_carte_pl2_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.p2_maine_carte
                        self.curr_menu.display_menu()

                #bouton menu cartes
                if self.curr_menu == self.p1_maine_carte:
                    if self.p1_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.curr_menu = Game
                if self.curr_menu == self.p2_maine_carte:
                    if self.p2_maine_carte.close_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        self.curr_menu = Game


                # Button main menu
                if self.main_menu.opion_button_rect.collidepoint(pygame.mouse.get_pos()):
                    self.curr_menu = self.options
                    self.curr_menu.display_menu()
                if self.curr_menu == self.main_menu:
                    if self.main_menu.play_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu = self.select_player
                        self.curr_menu.display_menu()
                    if self.main_menu.exit_button_rect.collidepoint(pygame.mouse.get_pos()):
                        self.running, self.playing = False, False
                        self.curr_menu.run_display = False
                        pygame.quit()
                if self.curr_menu == self.options:
                    if self.options.close_option_rect.collidepoint(pygame.mouse.get_pos()):
                        self.curr_menu.run_display = False
                        if self.select_player_confirme:
                            self.curr_menu = self.select_player
                        else:
                            self.curr_menu = self.main_menu


                # button option#

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
                                self.player1.caractere = Liam("Liam", "mcWarren", "populaire", "jeune", "M", "Le mercenaire")
                                self.select_player.player1 = "Liam"
                            else:
                                self.player2.caractere = Liam("Liam", "mcWarren", "populaire", "jeune", "M", "Le mercenaire")
                                self.select_player.player2 = "Liam"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_ambre_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.ambre_select == False and self.select_player.player2 == False:
                            self.select_player.carte_ambre = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.ambre_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Ambre("Ambre", "de Croy", "noble", "jeune", "F", "La demoiselle")
                                self.select_player.player1 = "Ambre"
                                
                            else:
                                self.player2.caractere = Ambre("Ambre", "deCroy", "noble", "jeune", "F", "La demoiselle" )
                                self.select_player.player2 = "Ambre"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_alfred_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.alfred_select == False and self.select_player.player2 == False:
                            self.select_player.carte_alfred = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.alfred_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Alfred("Alfred", "Heimsworth", "noble", "vieux", "M", "Le majordome")
                                self.select_player.player1 = "Alfred"
                            else:
                                self.player2.caractere = Alfred("Alfred", "Heimsworth", "noble", "vieux", "M", "Le majordome")
                                self.select_player.player2 = "Alfred"
                        
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_crystal_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.crystal_select == False and self.select_player.player2 == False:
                            self.select_player.carte_crystal = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.crystal_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Crystal("Crystal", "Devereux", "populaire", "vieux", "F", "Le requin")
                                self.select_player.player1 = "Crystal"

                            else:
                                self.player2.caractere = Crystal("Crystal", "Devereux", "populaire", "vieux", "F", "Le requin")
                                self.select_player.player2 = "Crystal"


    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)