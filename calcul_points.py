import pygame

class Calcul_points():
    def __init__(self, game):
        self.game = game
        self.point_p1 = 0
        self.point_p2 = 0
        self.win = None
        self.menux, self.menuy = self.game.mid_w, self.game.mid_h + 50
        self.textx, self.texty = self.game.mid_w, self.game.mid_h - 50
        self.bg_end = pygame.image.load("assets/win/bg_fin.png")
        self.button_menu = pygame.image.load("assets/win/button_menu.png")
        self.button_menu_rect = self.button_menu.get_rect()
        self.button_menu_rect.center = (self.menux, self.menuy)

    def calcul_points(self):
        longeur_phrase_p1 = len(self.game.player1.mots)
        self.point_p1 += longeur_phrase_p1 * 50
        for mot in self.game.player1.mots:
            for mot2 in self.game.player2.caractere.list_mot_tres_efficace:
                if mot.name == mot2.name:
                    self.point_p1 += 100 * self.game.player1.bonus_publique
            for mot3 in self.game.player2.caractere.list_mot_efficace:
                if mot.name == mot3.name:
                    self.point_p1 += 50 * self.game.player1.bonus_publique
            for mot4 in self.game.player2.caractere.list_mot_inneficace:
                if mot.name == mot4.name:
                    self.point_p1 -= 25 * self.game.player1.bonus_publique
        point_de_confiance = (self.game.player1.jauge_de_confiance / 100) + 1
        self.point_p1 = self.point_p1 * point_de_confiance

        longeur_phrase_p2 = len(self.game.player2.mots)
        self.point_p2 += longeur_phrase_p2 * 50
        for mot in self.game.player2.mots:
            for mot2 in self.game.player1.caractere.list_mot_tres_efficace:
                if mot.name == mot2.name:
                    self.point_p2 += 100 * self.game.player2.bonus_publique
            for mot3 in self.game.player1.caractere.list_mot_efficace:
                if mot.name == mot3.name:
                    self.point_p2 += 50 * self.game.player2.bonus_publique
            for mot4 in self.game.player1.caractere.list_mot_inneficace:
                if mot.name == mot4.name:
                    self.point_p2 -= 25 * self.game.player2.bonus_publique
        point_de_confiance = (self.game.player1.jauge_de_confiance / 100) + 1
        self.point_p2 = self.point_p2 * point_de_confiance

    def who_win(self):
        if self.point_p1 > self.point_p2:
            if self.game.player1.win1 == True:
                self.game.player1.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl1, self.game.button_victoire2_pl1_rect)
                self.game.update_screen()
                self.win = "p1"
                self.display_end()
            else:
                self.game.player1.win1 = True
                self.game.init_manche()
        elif self.point_p2 > self.point_p1:
            if self.game.player2.win1 == True:
                self.game.player2.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl2, self.game.button_victoire2_pl2_rect)
                self.game.update_screen()
                self.win = "p2"
                self.display_end()
            else:
                self.game.player2.win1 = True
                self.game.init_manche()
        else:
            if self.game.player1.win1 == True and self.game.player2.win1 == True:
                self.game.player1.win2 = True
                self.game.player2.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl1, self.game.button_victoire2_pl1_rect)
                self.game.display.blit(self.game.button_victoire2_pl2, self.game.button_victoire2_pl2_rect)
                self.game.update_screen()
                self.win = "p1 p2"
                self.display_end()
            if self.game.player1.win1 == True:
                self.game.player1.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl1, self.game.button_victoire2_pl1_rect)
                self.game.update_screen()
                self.win = "p1"
                self.display_end()
            else:
                self.game.player1.win1 = True
                self.game.init_manche()

            if self.game.player2.win1 == True:
                self.game.player2.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl2, self.game.button_victoire2_pl2_rect)
                self.game.update_screen()
                self.win = "p2"
                self.display_end()
            else:
                self.game.player2.win1 = True
                self.game.init_manche()

    def display_end(self):
        self.run_display = True
        while self.run_display:
            self.game.display.blit(self.bg_end, (0,0))
            if self.win == "p1":
                self.game.draw_text("le joueur 1 a gagné !", 30, (0,0,0), self.textx, self.texty, self.game.font_name)
            elif self.win == "p2":
                self.game.draw_text("le joueur 2 a gagné !", 30, (0,0,0), self.textx, self.texty, self.game.font_name)
            elif self.win == "p1 p2":
                self.game.draw_text("Les deux joueur sont ex æquo !", 30, (0,0,0), self.textx, self.texty, self.game.font_name)
            self.game.display.blit(self.button_menu, self.button_menu_rect)
            self.game.check_events()
            self.game.update_screen()