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

        self.pas_efficace1 = False
        self.pas_efficace2 = False
        self.pas_efficace3 = False
        self.pas_efficace4 = False
        self.pas_efficace5 = False
        self.pas_efficace6 = False
        self.pas_efficace7 = False
        self.pas_efficace8 = False
        self.pas_efficace9 = False
        self.pas_efficace10 = False
        self.pas_efficace_img = pygame.image.load("assets/game/mots_pas_efficace.png")
        self.efficace1 = False
        self.efficace2 = False
        self.efficace3 = False
        self.efficace4 = False
        self.efficace5 = False
        self.efficace6 = False
        self.efficace7 = False
        self.efficace8 = False
        self.efficace9 = False
        self.efficace10 = False
        self.efficace_img = pygame.image.load("assets/game/mots_efficace.png")

        self.mot1x, self.mot1y = self.game.mid_w -   5, self.game.mid_h - 339
        self.mot2x, self.mot2y = self.game.mid_w -   5, self.game.mid_h - 296
        self.mot3x, self.mot3y = self.game.mid_w -   5, self.game.mid_h - 253
        self.mot4x, self.mot4y = self.game.mid_w -   5, self.game.mid_h - 210
        self.mot5x, self.mot5y = self.game.mid_w -   5, self.game.mid_h - 167
        self.mot6x, self.mot6y = self.game.mid_w -   5, self.game.mid_h - 124
        self.mot7x, self.mot7y = self.game.mid_w -   5, self.game.mid_h - 81
        self.mot8x, self.mot8y = self.game.mid_w -   5, self.game.mid_h - 38
        self.mot9x, self.mot9y = self.game.mid_w -   5, self.game.mid_h + 5
        self.mot10x, self.mot10y = self.game.mid_w - 5, self.game.mid_h + 48

    def select_mots(self):
        self.choix_mot1 = random.randint(0, len(self.liste_mots.groupe_nominaux)-1)
        self.mot1 = self.liste_mots.groupe_nominaux[self.choix_mot1]
        del self.liste_mots.groupe_nominaux[self.choix_mot1]
        self.choix_mot2 = random.randint(0, len(self.liste_mots.groupe_nominaux)-1)
        self.mot2 = self.liste_mots.groupe_nominaux[self.choix_mot2]
        while self.mot2.name == self.mot1.name:
            self.choix_mot2 = random.randint(0, len(self.liste_mots.groupe_nominaux)-1)
            self.mot2 = self.liste_mots.groupe_nominaux[self.choix_mot2]
        del self.liste_mots.groupe_nominaux[self.choix_mot2]
        self.choix_mot3 = random.randint(0, len(self.liste_mots.groupe_nominaux)-1)
        self.mot3 = self.liste_mots.groupe_nominaux[self.choix_mot3]
        while self.mot3.name == self.mot1.name or self.mot3.name == self.mot2.name:
            self.choix_mot3 = random.randint(0, len(self.liste_mots.groupe_nominaux)-1)
            self.mot3 = self.liste_mots.groupe_nominaux[self.choix_mot3]
        del self.liste_mots.groupe_nominaux[self.choix_mot3]
        self.choix_mot4 = random.randint(0, len(self.liste_mots.complements)-1)
        self.mot4 = self.liste_mots.complements[self.choix_mot4]
        while self.mot4.name == self.mot1.name or self.mot4.name == self.mot2.name or self.mot4.name == self.mot3.name:
            self.choix_mot4 = random.randint(0, len(self.liste_mots.complements)-1)
            self.mot4 = self.liste_mots.groupe_nominaux[self.choix_mot4]
        del self.liste_mots.complements[self.choix_mot4]
        self.choix_mot5 = random.randint(0, len(self.liste_mots.complements)-1)
        self.mot5 = self.liste_mots.complements[self.choix_mot5]
        while self.choix_mot5 == self.choix_mot1 or self.choix_mot5 == self.choix_mot2 or self.choix_mot5 == self.choix_mot3 or self.choix_mot5 == self.choix_mot4:
            self.choix_mot5 = random.randint(0, len(self.liste_mots.complements)-1)
            self.mot5 = self.liste_mots.complements[self.choix_mot5]
        del self.liste_mots.complements[self.choix_mot5]
        self.choix_mot6 = random.randint(0, len(self.liste_mots.complements)-1)
        self.mot6 = self.liste_mots.complements[self.choix_mot6]
        while self.mot6.name == self.mot1.name or self.mot6.name == self.mot2.name or self.mot6.name == self.mot3.name or self.mot6.name == self.mot4.name or self.mot6.name == self.mot5.name:
            self.choix_mot6 = random.randint(0, len(self.liste_mots.complements)-1)
            self.mot6 = self.liste_mots.complements[self.choix_mot6]
        del self.liste_mots.complements[self.choix_mot6]
        self.choix_mot7 = random.randint(0, len(self.liste_mots.groupe_verbaux)-1)
        self.mot7 = self.liste_mots.groupe_verbaux[self.choix_mot7]
        while self.mot7.name == self.mot4.name or self.mot7.name == self.mot5.name or self.mot7.name == self.mot6.name:
            self.choix_mot7 = random.randint(0, len(self.liste_mots.groupe_verbaux)-1)
            self.mot7 = self.liste_mots.groupe_verbaux[self.choix_mot7]
        del self.liste_mots.groupe_verbaux[self.choix_mot7]
        self.choix_mot8 = random.randint(0, len(self.liste_mots.groupe_verbaux)-1)
        self.mot8 = self.liste_mots.groupe_verbaux[self.choix_mot8]
        while self.mot8.name == self.mot4.name or self.mot8.name == self.mot5.name or self.mot8.name == self.mot6.name or self.mot8.name == self.mot7.name:
            self.choix_mot8 = random.randint(0, len(self.liste_mots.groupe_verbaux)-1)
            self.mot8 = self.liste_mots.groupe_verbaux[self.choix_mot8]
        del self.liste_mots.groupe_verbaux[self.choix_mot8]
        self.choix_mot9 = random.randint(0, len(self.liste_mots.conjonction_de_coordination)-1)
        self.mot9 = self.liste_mots.conjonction_de_coordination[self.choix_mot9]
        self.choix_mot10 = random.randint(0, len(self.liste_mots.conjonction_de_coordination)-1)
        self.mot10 = self.liste_mots.conjonction_de_coordination[self.choix_mot10]
        while self.mot10.name == self.mot9.name:
            self.choix_mot10 = random.randint(0, len(self.liste_mots.conjonction_de_coordination)-1)
            self.mot10 = self.liste_mots.conjonction_de_coordination[self.choix_mot10]

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









