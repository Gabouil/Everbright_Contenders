from menu import *
from selectPlayer import *
from player1 import *
from player2 import *


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
        self.player2 = Player2(self)

        #import de game dans la class selctplayer
        self.select_player = SelectPlayer(self)
        self.select_player_confirme = False

        self.curr_menu = self.main_menu

        #position des images
        self.optionx, self.optiony = self.DISPLAY_W - 80, self.DISPLAY_H - 60
        self.name_player1x, self.name_player1y = self.mid_w, self.mid_h
        self.name_player2x, self.name_player2y = self.mid_w, self.mid_h
        self.button_carte_pl1x, self.button_carte_pl1y = self.mid_w - 360, self.mid_h + 250

        #Bouton du jeux
        self.button_carte_pl1 = pygame.image.load("assets/game/bouton_menu_carte.png")
        self.button_carte_pl1_rect = self.button_carte_pl1.get_rect()
        self.button_carte_pl1_rect.center = (self.button_carte_pl1x, self.button_carte_pl1y)

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

    def init_manche(self):
        self.player1.main_cartes()
        self.player2.main_cartes()

    def game_loop(self):
        self.playing = True
        self.init_game()
        while self.playing:
            self.check_events()
            self.display.blit(self.background, (0, 0))
            self.draw_text(self.player1.caractere.firstname + "" + self.player1.caractere.name, 50, (250,0,0), self.name_player1x, self.name_player1y)
            self.display.blit(self.button_carte_pl1, self.button_carte_pl1_rect)
            self.display.blit(self.player1.sprit_player1, self.player1.sprit_player1_rect)
            self.display.blit(self.opion_button, self.opion_button_rect)
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
                                self.player1.caractere = Liam("Liam", "mcWarren", "populaire", "jeune", "M")
                                self.select_player.player1 = "Liam"
                            else:
                                self.player2.caractere = Liam("Liam", "mcWarren", "populaire", "jeune", "M")
                                self.select_player.player2 = "Liam"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_ambre_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.ambre_select == False and self.select_player.player2 == False:
                            self.select_player.carte_ambre = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.ambre_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Ambre("Ambre", "deCroy", "noble", "jeune", "F")
                                self.select_player.player1 = "Ambre"
                                
                            else:
                                self.player2.caractere = Ambre("Ambre", "deCroy", "noble", "jeune", "F")
                                self.select_player.player2 = "Ambre"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_alfred_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.alfred_select == False and self.select_player.player2 == False:
                            self.select_player.carte_alfred = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.alfred_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Alfred("Alfred", "Heimsworth", "noble", "vieux", "M")
                                self.select_player.player1 = "Alfred"
                            else:
                                self.player2.caractere = Alfred("Alfred", "Heimsworth", "noble", "vieux", "M")
                                self.select_player.player2 = "Alfred"
                        
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_crystal_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.crystal_select == False and self.select_player.player2 == False:
                            self.select_player.carte_crystal = pygame.image.load("assets/cartes/dos_carte_or.png")
                            self.select_player.crystal_select = True
                            if self.select_player.player1 == False:
                                self.player1.caractere = Crystal("Crystal", "Devereux", "populaire", "vieux", "F")
                                self.select_player.player1 = "Crystal"

                            else:
                                self.player2.caractere = Crystal("Crystal", "Devereux", "populaire", "vieux", "F")
                                self.select_player.player2 = "Crystal"


    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)