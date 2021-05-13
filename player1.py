from caractere import *
from random import randint
import pygame


class Player1():
    def __init__(self,game):
        self.game = game
        self.list_boutdephrase = [1, 2, 3]
        self.jauge_de_confiance = 0
        self.bonus_publique = 5
        self.caractere = None
        self.carte1 = 0
        self.number_carte1 = 0
        self.carte2 = 0
        self.number_carte2 = 0
        self.carte3 = 0
        self.number_carte3 = 0
        self.win1 = None
        self.win2 = None
        self.carte_gratuit = False
        self.carte_double = False
        self.carte_chance = False
        self.carte_oblige = False
        self.second_vie = False
        self.exodio = EXODIO(self.game, "Exodio", "Divin")

        self.spritx, self.sprity = self.game.mid_w - 550, self.game.mid_h - 100


        self.pcarte1x, self.pcarte1y = self.game.mid_w + 380, self.game.mid_h
        self.pcarte2x, self.pcarte2y = self.game.mid_w, self.game.mid_h
        self.pcarte3x, self.pcarte3y = self.game.mid_w - 380, self.game.mid_h

    def charge_sprit(self):
        self.sprit_player1 = self.caractere.img
        self.sprit_player1_rect = self.sprit_player1.get_rect()
        self.sprit_player1_rect.center = (self.spritx, self.sprity)
    
    #def influence_publique(self):
        
        

        

    def main_cartes(self):
        self.number_carte1 = randint(0, 2)
        # self.carte1 = self.caractere.list_cartes[self.number_carte1]
        self.carte1 = self.caractere.list_cartes[6]
        self.number_carte2 = randint(3, 14)
        while self.number_carte2 == self.number_carte1:
            self.number_carte2 = randint(3, 14)
        # self.carte2 = self.caractere.list_cartes[self.number_carte2]
        self.carte2 = self.caractere.list_cartes[11]
        self.number_carte3 = randint(3, 14)
        while self.number_carte3 == self.number_carte2:
            self.number_carte3 = randint(3, 14)
        # self.carte3 = self.caractere.list_cartes[self.number_carte3]
        self.carte3 = self.caractere.list_cartes[2]

    def main_cartes_round(self):
        if self.carte1 == None:
            self.number_carte1 = randint(0, 14)
            self.carte1 = self.caractere.list_cartes[self.number_carte1]
        if self.carte2 == None:
            self.number_carte2 = randint(0, 14)
            self.carte2 = self.caractere.list_cartes[self.number_carte2]
        if self.carte3 == None:
            self.number_carte3 = randint(0, 14)
            self.carte3 = self.caractere.list_cartes[self.number_carte3]

class Main_carte_p1(Player1):
    def __init__(self, game):
        Player1.__init__(self, game)
        self.background = pygame.image.load("assets/game/menu_cartes_bg.png")
        self.closex, self.closey = self.game.mid_w + 470 , self.game.mid_h - 300
        self.close_button = pygame.image.load("assets/game/close_menu_carte.png")
        self.close_button_rect = self.close_button.get_rect()
        self.close_button_rect.center = (self.closex, self.closey)
        self.carte_none = pygame.image.load("assets/cartes/dos_carte_fer.png")


    def display_menu(self):
        self.run_display = True
        self.game.charge_carte_p1()
        self.no_option = True
        while self.run_display:
            self.game.display.blit(self.background, (0,0))
            self.game.display.blit(self.close_button, self.close_button_rect)
            self.game.check_events()
            self.game.display.blit(self.game.button_carte1, self.game.button_carte1_rect)
            self.game.display.blit(self.game.button_carte2, self.game.button_carte2_rect)
            self.game.display.blit(self.game.button_carte3, self.game.button_carte3_rect)
            self.game.update_screen()