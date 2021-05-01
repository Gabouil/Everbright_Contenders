from menu import *
from selectPlayer import *


class Game():
    def __init__(self):
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        self.font_name = 'Seagram.ttf'

        #import de game dans les class menu
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.credits = CreditsMenu(self)

        #import de game dans la class selctplayer
        self.select_player = SelectPlayer(self)
        self.select_player_confirme = False

        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            pass

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    if self.select_player.carte_liam_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.liam_select == False and self.select_player.player2 == False:
                            self.select_player.carte_liam = pygame.image.load("assets/select_player/dos_carte_or.png")
                            self.select_player.liam_select = True
                            if self.select_player.player1 == False:
                                self.select_player.player1 = "Liam"
                            else:
                                self.select_player.player2 = "Liam"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_ambre_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.ambre_select == False and self.select_player.player2 == False:
                            self.select_player.carte_ambre = pygame.image.load("assets/select_player/dos_carte_or.png")
                            self.select_player.ambre_select = True
                            if self.select_player.player1 == False:
                                self.select_player.player1 = "Ambre"
                            else:
                                self.select_player.player2 = "Ambre"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_alfred_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.alfred_select == False and self.select_player.player2 == False:
                            self.select_player.carte_alfred = pygame.image.load("assets/select_player/dos_carte_or.png")
                            self.select_player.alfred_select = True
                            if self.select_player.player1 == False:
                                self.select_player.player1 = "Alfred"
                            else:
                                self.select_player.player2 = "Alfred"
                            print(self.select_player.player1, self.select_player.player2)
                    if self.select_player.carte_crystal_rect.collidepoint(pygame.mouse.get_pos()):
                        if self.select_player.crystal_select == False and self.select_player.player2 == False:
                            self.select_player.carte_crystal = pygame.image.load("assets/select_player/dos_carte_or.png")
                            self.select_player.crystal_select = True
                            if self.select_player.player1 == False:
                                self.select_player.player1 = "Crystal"
                            else:
                                self.select_player.player2 = "Crystal"
                            print(self.select_player.player1, self.select_player.player2)


    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)