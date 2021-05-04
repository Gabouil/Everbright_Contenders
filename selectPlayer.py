import pygame

class SelectPlayer():
    def __init__(self, game):
        self.game = game
        self.run_display = True
        self.player1, self.player2 = False, False
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.background = pygame.image.load("assets/select_player/bg.png")

        self.startx, self.starty = self.mid_w, self.mid_h + 390
        self.player_tourx, self.player_toury = self.mid_w, self.mid_h + 390
        self.player1x, self.player1y = self.mid_w - 440, self.mid_h - 305
        self.player2x, self.player2y = self.mid_w + 490, self.mid_h - 305

        self.liamx, self.liamy = self.mid_w - 485, self.mid_h - 20
        self.ambrex, self.ambrey = self.mid_w - 165, self.mid_h - 20
        self.alfredx, self.alfredy = self.mid_w + 165, self.mid_h - 20
        self.crystalx, self.crystaly = self.mid_w + 490, self.mid_h - 20

        self.button_start = pygame.image.load("assets/select_player/button_start.png")

        self.button_start_rect = self.button_start.get_rect()
        self.button_start_rect.center = (self.startx, self.starty)

        self.carte_liam = pygame.image.load("assets/cartes/carte_liam.png")
        self.carte_liam_rect = self.carte_liam.get_rect()
        self.carte_liam_rect.center = (self.liamx, self.liamy)
        self.liam_select = False

        self.carte_ambre = pygame.image.load("assets/cartes/carte_ambre.png")
        self.carte_ambre_rect = self.carte_ambre.get_rect()
        self.carte_ambre_rect.center = (self.ambrex, self.ambrey)
        self.ambre_select = False

        self.carte_alfred = pygame.image.load("assets/cartes/carte_alfred.png")
        self.carte_alfred_rect = self.carte_alfred.get_rect()
        self.carte_alfred_rect.center = (self.alfredx, self.alfredy)
        self.alfred_select = False

        self.carte_crystal = pygame.image.load("assets/cartes/carte_crystal.png")
        self.carte_crystal_rect = self.carte_crystal.get_rect()
        self.carte_crystal_rect.center = (self.crystalx, self.crystaly)
        self.crystal_select = False




    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill((0,0,0))
            self.game.display.blit(self.background, (0, 0))
            self.game.display.blit(self.carte_liam, self.carte_liam_rect)
            self.game.display.blit(self.carte_ambre, self.carte_ambre_rect)
            self.game.display.blit(self.carte_alfred, self.carte_alfred_rect)
            self.game.display.blit(self.carte_crystal, self.carte_crystal_rect)
            self.check_carte()
            self.game.check_events()
            self.game.display.blit(self.game.main_menu.opion_button, self.game.main_menu.opion_button_rect)
            self.game.main_menu.update_screen()

    def check_carte(self):
        if self.player1:
            self.game.draw_text(self.player1, 20, (0, 0, 0), self.player1x, self.player1y)
            self.game.draw_text("Choix du joueur 2", 20, (0, 0, 0), self.player_tourx, self.player_toury)
            if self.player2:
                self.game.draw_text(self.player2, 20, (0, 0, 0), self.player2x, self.player2y)
                self.game.display.blit(self.button_start, self.button_start_rect)

        else:
            self.game.draw_text("Choix du joueur 1", 20, (0, 0, 0), self.player_tourx, self.player_toury)
