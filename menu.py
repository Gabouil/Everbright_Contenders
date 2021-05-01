import pygame

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.background = pygame.image.load("assets/menu/bg.png")
        self.option_back = pygame.image.load("assets/option_menu.png")

    def update_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.optionx, self.optiony = self.game.DISPLAY_W - 80, self.game.DISPLAY_H - 60
        self.playx, self.playy = self.mid_w, self.mid_h
        self.rulesx, self.rulesy = self.mid_w, self.mid_h + 100
        self.aboutx, self.abouty = self.mid_w, self.mid_h + 200
        self.exitx, self.exity = self.mid_w, self.mid_h + 300

        #draw button
        self.opion_button = pygame.image.load("assets/option_button.png")
        self.opion_button_rect = self.opion_button.get_rect()
        self.opion_button_rect.center = (self.optionx, self.optiony)

        self.play_button = pygame.image.load("assets/menu/button_play.png")
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.center = (self.playx, self.playy)

        self.rules_button = pygame.image.load("assets/menu/button_rules.png")
        self.rules_button_rect = self.rules_button.get_rect()
        self.rules_button_rect.center = (self.rulesx, self.rulesy)

        self.about_button = pygame.image.load("assets/menu/button_about.png")
        self.about_button_rect = self.about_button.get_rect()
        self.about_button_rect.center = (self.aboutx, self.abouty)

        self.exit_button = pygame.image.load("assets/menu/button_exit.png")
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.center = (self.exitx, self.exity)

    def display_menu(self):
        pygame.mixer.music.load("song/main_menu_theme.mp3")
        pygame.mixer.music.play(0)
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.background, (0, 0))
            self.game.check_events()
            self.game.display.blit(self.play_button, self.play_button_rect)
            self.game.display.blit(self.rules_button, self.rules_button_rect)
            self.game.display.blit(self.about_button, self.about_button_rect)
            self.game.display.blit(self.exit_button, self.exit_button_rect)
            self.game.display.blit(self.opion_button, self.opion_button_rect)
            self.update_screen()

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.volx, self.voly = self.mid_w, self.mid_h + 10
        self.closex, self.closey = self.game.DISPLAY_W - 300, self.mid_h - 210
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 100
        self.songx, self.songy = self.mid_w + 135, self.mid_h - 105
        self.songPx, self.songPy = self.mid_w + 265, self.mid_h - 105
        self.songMx, self.songMy = self.mid_w, self.mid_h - 98
        self.rulesx, self.rulesy = self.mid_w, self.mid_h + 150


        #check box
        self.song_check_checked = False
        self.song_check = pygame.image.load("assets/button_check_false.png")
        self.song_check_rect = self.song_check.get_rect()
        self.song_check_rect.center = (self.volx, self.voly)

        self.close_option = pygame.image.load("assets/close.png")
        self.close_option_rect = self.close_option.get_rect()
        self.close_option_rect.center = (self.closex, self.closey)

        self.song = pygame.image.load("assets/song_5.png")
        self.song_rect = self.song.get_rect()
        self.song_rect.center = (self.songx, self.songy)
        self.songP = pygame.image.load("assets/song+.png")
        self.songP_rect = self.songP.get_rect()
        self.songP_rect.center = (self.songPx, self.songPy)
        self.songM = pygame.image.load("assets/song-.png")
        self.songM_rect = self.songM.get_rect()
        self.songM_rect.center = (self.songMx, self.songMy)
        self.song_niv = 0.5

        self.rules_button = pygame.image.load("assets/menu/button_rules.png")
        self.rules_button_rect = self.rules_button.get_rect()
        self.rules_button_rect.center = (self.rulesx, self.rulesy)

    def checked_verif(self):
        if self.song_check_checked:
            self.song_check = pygame.image.load("assets/button_check_true.png")
            pygame.mixer.music.set_volume(0)
            self.song_check_rect.center = (self.volx - 7, self.voly - 14)
        else:
            self.song_check = pygame.image.load("assets/button_check_false.png")
            pygame.mixer.music.set_volume(self.song_niv)
            self.song_check_rect.center = (self.volx, self.voly)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.option_back, (0, 0))
            self.game.check_events()
            self.checked_verif()
            self.game.display.blit(self.song_check, self.song_check_rect)
            self.game.display.blit(self.songP, self.songP_rect)
            self.game.display.blit(self.song, self.song_rect)
            self.game.display.blit(self.songM, self.songM_rect)
            self.game.display.blit(self.rules_button, self.rules_button_rect)
            self.game.display.blit(self.close_option, self.close_option_rect)
            self.update_screen()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill((0,0,0))
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by me', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.update_screen()