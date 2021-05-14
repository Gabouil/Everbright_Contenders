import  pygame
import random

class Game_mots():
    def __init__(self, game):
        self.game = game
        self.liste_mots = game.Liste_mot(game)
        self.mot1 = None
        self.mot2 = None
        self.mot3 = None
        self.mot4 = None
        self.mot5 = None
        self.mot6 = None
        self.mot7 = None
        self.mot8 = None
        self.mot9 = None
        self.mot10 = None
        self.choix_mot1 = None
        self.choix_mot2 = None
        self.choix_mot3 = None
        self.choix_mot4 = None
        self.choix_mot5 = None
        self.choix_mot6 = None
        self.choix_mot7 = None
        self.choix_mot8 = None
        self.choix_mot9 = None
        self.choix_mot10 = None

        self.mot1x, self.mot1y = self.game.mid_w -   20, self.game.mid_h - 328
        self.mot2x, self.mot2y = self.game.mid_w -   20, self.game.mid_h - 285
        self.mot3x, self.mot3y = self.game.mid_w -   20, self.game.mid_h - 242
        self.mot4x, self.mot4y = self.game.mid_w -   20, self.game.mid_h - 199
        self.mot5x, self.mot5y = self.game.mid_w -   20, self.game.mid_h - 156
        self.mot6x, self.mot6y = self.game.mid_w -   20, self.game.mid_h - 113
        self.mot7x, self.mot7y = self.game.mid_w -   20, self.game.mid_h - 70
        self.mot8x, self.mot8y = self.game.mid_w -   20, self.game.mid_h - 27
        self.mot9x, self.mot9y = self.game.mid_w -   20, self.game.mid_h + 16
        self.mot10x, self.mot10y = self.game.mid_w - 20, self.game.mid_h + 59

    def select_mots(self):
        self.choix_mot1 = random.randint(0, 35)
        self.mot1 = self.liste_mots.liste_mots[self.choix_mot1]
        self.choix_mot2 = random.randint(0, 35)
        while self.choix_mot2 == self.choix_mot1:
            self.choix_mot2 = random.randint(0, 35)
        self.mot2 = self.liste_mots.liste_mots[self.choix_mot2]
        self.choix_mot3 = random.randint(0, 35)
        while self.choix_mot3 == self.choix_mot1 or self.choix_mot3 == self.choix_mot2:
            self.choix_mot3 = random.randint(0, 35)
        self.mot3 = self.liste_mots.liste_mots[self.choix_mot3]
        self.choix_mot4 = random.randint(14, 52)
        while self.choix_mot4 == self.choix_mot1 or self.choix_mot4 == self.choix_mot2 or self.choix_mot4 == self.choix_mot3:
            self.choix_mot4 = random.randint(14, 52)
        self.mot4 = self.liste_mots.liste_mots[self.choix_mot4]
        self.choix_mot5 = random.randint(14, 52)
        while self.choix_mot5 == self.choix_mot1 or self.choix_mot5 == self.choix_mot2 or self.choix_mot5 == self.choix_mot3 or self.choix_mot5 == self.choix_mot4:
            self.choix_mot5 = random.randint(14, 52)
        self.mot5 = self.liste_mots.liste_mots[self.choix_mot5]
        self.choix_mot6 = random.randint(14, 52)
        while self.choix_mot6 == self.choix_mot1 or self.choix_mot6 == self.choix_mot2 or self.choix_mot6 == self.choix_mot3 or self.choix_mot6 == self.choix_mot4 or self.choix_mot6 == self.choix_mot5:
            self.choix_mot6 = random.randint(14, 52)
        self.mot6 = self.liste_mots.liste_mots[self.choix_mot6]
        self.choix_mot7 = random.randint(48, 66)
        while self.choix_mot7 == self.choix_mot4 or self.choix_mot7 == self.choix_mot5 or self.choix_mot7 == self.choix_mot6:
            self.choix_mot7 = random.randint(48, 66)
        self.mot7 = self.liste_mots.liste_mots[self.choix_mot7]
        self.choix_mot8 = random.randint(48, 66)
        while self.choix_mot8 == self.choix_mot4 or self.choix_mot8 == self.choix_mot5 or self.choix_mot8 == self.choix_mot6 or self.choix_mot8 == self.choix_mot7:
            self.choix_mot8 = random.randint(48, 66)
        self.mot8 = self.liste_mots.liste_mots[self.choix_mot8]
        self.choix_mot9 = random.randint(67, 73)
        self.mot9 = self.liste_mots.liste_mots[self.choix_mot9]
        self.choix_mot10 = random.randint(67, 73)
        while self.choix_mot10 == self.choix_mot9:
            self.choix_mot10 = random.randint(67, 73)
        self.mot10 = self.liste_mots.liste_mots[self.choix_mot10]

    def charge_mots(self):
        self.button_mot1 = self.mot1.img
        self.button_mot1_rect = self.button_mot1.get_rect()
        self.button_mot1_rect.center = (self.mot1x, self.mot1y)
        self.button_mot2 = self.mot2.img
        self.button_mot2_rect = self.button_mot2.get_rect()
        self.button_mot2_rect.center = (self.mot2x, self.mot2y)
        self.button_mot3 = self.mot3.img
        self.button_mot3_rect = self.button_mot3.get_rect()
        self.button_mot3_rect.center = (self.mot3x, self.mot3y)
        self.button_mot4 = self.mot4.img
        self.button_mot4_rect = self.button_mot4.get_rect()
        self.button_mot4_rect.center = (self.mot4x, self.mot4y)
        self.button_mot5 = self.mot5.img
        self.button_mot5_rect = self.button_mot5.get_rect()
        self.button_mot5_rect.center = (self.mot5x, self.mot5y)
        self.button_mot6 = self.mot6.img
        self.button_mot6_rect = self.button_mot6.get_rect()
        self.button_mot6_rect.center = (self.mot6x, self.mot6y)
        self.button_mot7 = self.mot7.img
        self.button_mot7_rect = self.button_mot7.get_rect()
        self.button_mot7_rect.center = (self.mot7x, self.mot7y)
        self.button_mot8 = self.mot8.img
        self.button_mot8_rect = self.button_mot8.get_rect()
        self.button_mot8_rect.center = (self.mot8x, self.mot8y)
        self.button_mot9 = self.mot9.img
        self.button_mot9_rect = self.button_mot9.get_rect()
        self.button_mot9_rect.center = (self.mot9x, self.mot9y)
        self.button_mot10 = self.mot10.img
        self.button_mot10_rect = self.button_mot10.get_rect()
        self.button_mot10_rect.center = (self.mot10x, self.mot10y)









