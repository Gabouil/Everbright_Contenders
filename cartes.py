import random
import pygame
from game import *
from caractere import *
from sound import *

class Cartes :
    def __init__(self, game,  name, type):
        self.game = game
        self.DISPLAY_W, self.DISPLAY_H = 1440, 1024
        self.name = name
        self.type = type
        self.mid_w, self.mid_h = self.DISPLAY_W / 2, self.DISPLAY_H / 2
        self.cartex, self.cartey = self.mid_w, self.mid_h

    def carte_use(self):
        if self.game.carte_use == "carte1":
            self.game.player_turn.carte1 = None
        elif self.game.carte_use == "carte2":
            self.game.player_turn.carte2 = None
        elif self.game.carte_use == "carte3":
            self.game.player_turn.carte3 = None

class EXODIO(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/exodio.png")

        self.chance_play = 38

    def retour_du_dieu(self):
        chance = random.randint(1,100)
        if chance == self.chance_play:
            player = random.randint(1,2)
            if player == 1:
                self.game.player1.carte1 = self.game.player1.exodio
            elif player == 2:
                self.game.player2.carte1 = self.game.player2.exodio

    def effect_carte(self):
        chance_effect = random.randint(1,4)
        if chance_effect == 3 or chance_effect == 4:
            self.game.game_mots.select_mots()
            self.game.game_mots.charge_mots()
            self.game.update_screen()
            self.carte_use()
        elif chance_effect == 1:
            if self.game.player_turn.win1 == True:
                self.game.player_turn.win2 = True
                self.game.display.blit(self.game.button_victoire2_pl1, self.game.button_victoire2_pl1_rect)
                self.game.update_screen()
                self.win = "p1"
                self.game.calcul_points.display_end()
                self.game.init_manche()
            else:
                self.game.player_turn.win1 = True
            self.carte_use()
        elif chance_effect == 2:
            caractere = random.randint(1, 4)
            if caractere == 4:
                self.game.player_turn.carte1 = self.game.liam.list_cartes[0]
                self.game.player_turn.carte2 = self.game.liam.list_cartes[1]
                self.game.player_turn.carte3 = self.game.liam.list_cartes[2]
            if caractere == 2:
                self.game.player_turn.carte1 = self.game.ambre.list_cartes[0]
                self.game.player_turn.carte2 = self.game.ambre.list_cartes[1]
                self.game.player_turn.carte3 = self.game.ambre.list_cartes[2]
            if caractere == 3:
                self.game.player_turn.carte1 = self.game.alfred.list_cartes[0]
                self.game.player_turn.carte2 = self.game.alfred.list_cartes[1]
                self.game.player_turn.carte3 = self.game.alfred.list_cartes[2]
            if caractere == 1:
                self.game.player_turn.carte1 = self.game.crystal.list_cartes[0]
                self.game.player_turn.carte2 = self.game.crystal.list_cartes[1]
                self.game.player_turn.carte3 = self.game.crystal.list_cartes[2]
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


# carte unique
#Liam
class True_story(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/true_story.png")


    def effect_carte(self):
        if self.game.player_turn.caractere == self.game.liam:
            self.game.list_crowd.crowd = self.game.list_crowd.liste_crowd[0]
        if self.game.player_turn.caractere == self.game.alfred:
            self.game.list_crowd.crowd = self.game.list_crowd.liste_crowd[5]
        if self.game.player_turn.caractere == self.game.ambre:
            self.game.list_crowd.crowd = self.game.list_crowd.liste_crowd[1]
        if self.game.player_turn.caractere == self.game.crystal:
            self.game.list_crowd.crowd = self.game.list_crowd.liste_crowd[3]
        self.game.list_crowd.button_crowd = self.game.list_crowd.crowd.img
        self.game.list_crowd.change_crowd = False
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Peche_davarice(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/peche_davarice.png")

    def effect_carte(self):
        self.game.liam_avarice = True
        self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Gamin_des_rues(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/gamin_des_rues.png")

    def effect_carte(self):
        number = random.randint(15, 25)
        if self.game.player_not_turn.antie_vol == False:
            self.game.player_not_turn.jauge_de_confiance -= number
            self.game.player_turn.jauge_de_confiance += number
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Ambre
class Secret_familial(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/secret_famillial.png")


    def effect_carte(self):
        mot = random.randint(0,2)
        self.game.player_turn.mots.append(self.game.player_not_turn.caractere.list_mot_tres_efficace[mot])
        self.game.update_phrase()
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Regard_enjoleur(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/regard_enjoleur.png")


    def effect_carte(self):
        self.game.player_not_turn.carte_oblige = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Conseils_avisees(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/conseils_avisees.png")


    def effect_carte(self):
        choix = random.randint(1, 3)
        if choix == 1:
            self.game.player_not_turn.carte1 = None
        elif choix == 2:
            self.game.player_not_turn.carte2 = None
        elif choix == 3:
            self.game.player_not_turn.carte3 = None
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


#Alfred
class Cest_pas_au_vieux_singe(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/cest_pas_au_vieux_singe.png")


    def effect_carte(self):
        self.game.player_turn.antie_critique = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


class Seconde_vie(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/second_vie.png")


    def effect_carte(self):
        self.game.player_turn.second_vie = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Service_sur_mesure(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/service_sur_mesure.png")


    def effect_carte(self):
        self.game.player_turn.antie_vol = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Crystal
class Rhetorique_de_limperatrice(Cartes):
    def __init__(self, game, name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/rhetorique_de_limperatrice.png")


    def effect_carte(self):
        self.game.player_turn.mot_free = True
        self.carte_use()

class Sombre_formule(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sombre_formule.png")

    def effect_carte(self):
        del self.game.player_not_turn.mots[-1]
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Influence_mystique(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/influence_mystique.png")

    def main_cartes(self):
        self.number_carte1 = random.randint(0, 14)
        self.carte1_mystique = self.game.player_not_turn.caractere.list_cartes[self.number_carte1]
        self.number_carte2 = random.randint(0, 14)
        while self.number_carte2 == self.number_carte1:
            self.number_carte2 = random.randint(0, 14)
        self.carte2_mystique = self.game.player_not_turn.caractere.list_cartes[self.number_carte2]
        self.number_carte3 = random.randint(0, 14)
        while self.number_carte3 == self.number_carte2:
            self.number_carte3 = random.randint(0, 14)
        self.carte3_mystique = self.game.player_not_turn.caractere.list_cartes[self.number_carte3]

    def mystique_cartes(self):
        self.mystique_carte1 = self.carte1_mystique.img
        self.mystique_carte1_rect = self.mystique_carte1.get_rect()
        self.mystique_carte1_rect.center = (self.game.player_turn.pcarte1x, self.game.player_turn.pcarte1y)
        self.mystique_carte2 = self.carte2_mystique.img
        self.mystique_carte2_rect = self.mystique_carte2.get_rect()
        self.mystique_carte2_rect.center = (self.game.player_turn.pcarte2x, self.game.player_turn.pcarte2y)
        self.mystique_carte3 = self.carte3_mystique.img
        self.mystique_carte3_rect = self.mystique_carte3.get_rect()
        self.mystique_carte3_rect.center = (self.game.player_turn.pcarte3x, self.game.player_turn.pcarte3y)

    def display_mystique_cartes(self):
        self.run_display = True
        self.no_option = True
        self.mystique_cartes()
        while self.run_display:
            self.game.display.blit(self.game.p1_maine_carte.background, (0,0))
            self.check_events_mystique_carte()
            self.game.display.blit(self.mystique_carte1, self.mystique_carte1_rect)
            self.game.display.blit(self.mystique_carte2, self.mystique_carte2_rect)
            self.game.display.blit(self.mystique_carte3, self.mystique_carte3_rect)
            self.game.update_screen()

    def check_events_mystique_carte(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                if self.mystique_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.game.carte_use == "carte1":
                        self.game.player_turn.carte1 = self.carte1_mystique
                    elif self.game.carte_use == "carte2":
                        self.game.player_turn.carte2 = self.carte1_mystique
                    elif self.game.carte_use == "carte3":
                        self.game.player_turn.carte3 = self.carte1_mystique
                    self.run_display = False
                if self.mystique_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.game.carte_use == "carte1":
                        self.game.player_turn.carte1 = self.carte2_mystique
                    elif self.game.carte_use == "carte2":
                        self.game.player_turn.carte2 = self.carte2_mystique
                    elif self.game.carte_use == "carte3":
                        self.game.player_turn.carte3 = self.carte2_mystique
                    self.run_display = False
                if self.mystique_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                    if self.game.carte_use == "carte1":
                        self.game.player_turn.carte1 = self.carte3_mystique
                    elif self.game.carte_use == "carte2":
                        self.game.player_turn.carte2 = self.carte3_mystique
                    elif self.game.carte_use == "carte3":
                        self.game.player_turn.carte3 = self.carte3_mystique
                    self.run_display = False

    def effect_carte(self):
        self.main_cartes()
        self.display_mystique_cartes()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Cartes Comune
#Jeune
class Gout_du_risque(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/gout_du_risque.png")

    def effect_carte(self):
        if self.game.list_crowd.change_crowd:
            self.game.list_crowd.charge_crowd()
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


class Sante_de_fer(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_de_fer.png")

    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Adaptation(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/adaptation.png")

    def carte(self):
        choix_de_carte = random.randint(0, 14)
        if self.game.player_turn.carte1 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte1 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]
        elif self.game.player_turn.carte2 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte2 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]
        elif self.game.player_turn.carte3 == self.game.player_turn.caractere.cartes.Adaptation:
            self.game.player_turn.carte3 = self.game.player_not_turn.caractere.list_cartes[choix_de_carte]

    def effect_carte(self):
        if self.game.player_turn.carte_gratuit:
            self.game.player_turn.carte_gratuit = False
            self.carte()
        if self.game.player_turn.carte_double:
            if self.game.player_turn.jauge_de_confiance >= 30:
                self.game.player_turn.carte_double = False
                self.carte()
                self.game.player_turn.jauge_de_confiance -= 30
        elif self.game.player_turn.jauge_de_confiance >= 15:
            self.carte()
            self.game.player_turn.jauge_de_confiance -= 15
        if self.game.player_turn.play_two != True:
            self.game.end_turn()




class Esprit_vif(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/esprit_vif.png")

    def effect_carte(self):
        for mot in self.game.player_not_turn.caractere.list_mot_inneficace:
            if mot.name == self.game.game_mots.mot1.name:
                self.game.game_mots.pas_efficace1 = True
            if mot.name == self.game.game_mots.mot2.name:
                self.game.game_mots.pas_efficace2 = True
            if mot.name == self.game.game_mots.mot3.name:
                self.game.game_mots.pas_efficace3 = True
            if mot.name == self.game.game_mots.mot4.name:
                self.game.game_mots.pas_efficace4 = True
            if mot.name == self.game.game_mots.mot5.name:
                self.game.game_mots.pas_efficace5 = True
            if mot.name == self.game.game_mots.mot6.name:
                self.game.game_mots.pas_efficace6 = True
            if mot.name == self.game.game_mots.mot7.name:
                self.game.game_mots.pas_efficace7 = True
            if mot.name == self.game.game_mots.mot8.name:
                self.game.game_mots.pas_efficace8 = True
            if mot.name == self.game.game_mots.mot9.name:
                self.game.game_mots.pas_efficace9 = True
            if mot.name == self.game.game_mots.mot10.name:
                self.game.game_mots.pas_efficace10 = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#âgé
class Experience_de_lage(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/experience_de_lage.png")


    def effect_carte(self):
        self.game.player_turn.bonus_publique = 1
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Veteran(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/veteran.png")


    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Sante_fragile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sante_fragile.png")


    def effect_carte(self):
        chance = random.randint(1, 2)
        if chance == 1:
            self.game.player_turn.jauge_de_confiance += 20
            self.carte_use()
            if self.game.player_turn.play_two != True:
                self.game.end_turn()
        if chance == 2:
            self.game.player_turn.jauge_de_confiance -= 5
            self.carte_use()
            if self.game.player_turn.play_two != True:
                self.game.end_turn()


class Oeil_sage(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/oeil_sage.png")


    def effect_carte(self):
        for mot in self.game.player_not_turn.caractere.list_mot_efficace:
            if mot.name == self.game.game_mots.mot1.name:
                self.game.game_mots.efficace1 = True
            if mot.name == self.game.game_mots.mot2.name:
                self.game.game_mots.efficace2 = True
            if mot.name == self.game.game_mots.mot3.name:
                self.game.game_mots.efficace3 = True
            if mot.name == self.game.game_mots.mot4.name:
                self.game.game_mots.efficace4 = True
            if mot.name == self.game.game_mots.mot5.name:
                self.game.game_mots.efficace5 = True
            if mot.name == self.game.game_mots.mot6.name:
                self.game.game_mots.efficace6 = True
            if mot.name == self.game.game_mots.mot7.name:
                self.game.game_mots.efficace7 = True
            if mot.name == self.game.game_mots.mot8.name:
                self.game.game_mots.efficace8 = True
            if mot.name == self.game.game_mots.mot9.name:
                self.game.game_mots.efficace9 = True
            if mot.name == self.game.game_mots.mot10.name:
                self.game.game_mots.efficace10 = True

        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Homme
class Avantage_masculin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_masculin.png")


    def effect_carte(self):
        if self.game.player_not_turn.antie_vol == False:
            if self.game.player_not_turn.caractere.sexe == "F":
                self.game.player_not_turn.jauge_de_confiance -= 10
                self.game.player_turn.jauge_de_confiance += 10
            elif self.game.player_not_turn.caractere.sexe == "M":
                self.game.player_not_turn.jauge_de_confiance -= 5
                self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


class Tonalite_virile(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/tonalite_virile.png")


    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Sens_du_sacrifice(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/sens_du_sacrifice.png")


    def effect_carte(self):
        if self.game.player_turn.carte_gratuit:
            self.game.player_turn.carte_gratuit = False
            del self.game.player_not_turn.mots[-1]
        if self.game.player_turn.carte_double:
            if self.game.player_turn.jauge_de_confiance >= 20:
                self.game.player_turn.carte_double = False
                del self.game.player_not_turn.mots[-1]
                self.game.player_turn.jauge_de_confiance -= 20
        elif self.game.player_turn.jauge_de_confiance >= 10:
            del self.game.player_not_turn.mots[-1]
            self.game.player_turn.jauge_de_confiance -= 10
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Monotache(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/monotache.png")


    def effect_carte(self):
        self.game.player_turn.carte_gratuit = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Femme
class Avantage_feminin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_feminin.png")


    def effect_carte(self):
        if self.game.player_not_turn.antie_vol == False:
            if self.game.player_not_turn.caractere.sexe == "M":
                self.game.player_not_turn.jauge_de_confiance -= 10
                self.game.player_turn.jauge_de_confiance += 10
            elif self.game.player_not_turn.caractere.sexe == "F":
                self.game.player_not_turn.jauge_de_confiance -= 5
                self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Mauvaise_foi(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/mauvaise_foi.png")


    def effect_carte(self):
        if self.game.player_turn.carte_gratuit:
            self.game.player_turn.carte_gratuit = False
            self.game.player_not_turn.carte_double = True
            self.carte_use()
        elif self.game.player_turn.carte_double :
            if self.game.player_turn.jauge_de_confiance >= 10:
                self.game.player_not_turn.carte_double = True
                self.game.player_turn.carte_double = False
                self.game.player_turn.jauge_de_confiance -= 10
                self.carte_use()
        elif self.game.player_turn.jauge_de_confiance >= 5 or self.game.player_turn.carte_gratuit :
            self.game.player_not_turn.carte_double = True
            self.game.player_turn.jauge_de_confiance -= 5
            self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()


class Seduction(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/seduction.png")


    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 10
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Multitache(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/multitache.png")


    def effect_carte(self):
        self.game.player_turn.play_two = True
        self.carte_use()

#Noble
class Opulence(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/opulence.png")

    def opulence_cartes(self):
        if self.game.player_turn.carte1 == None:
            self.opulence_carte1 = self.game.p1_maine_carte.carte_none
        else:
            self.opulence_carte1 = self.game.player_turn.carte1.img
        self.opulence_carte1_rect = self.opulence_carte1.get_rect()
        self.opulence_carte1_rect.center = (self.game.player_turn.pcarte1x, self.game.player_turn.pcarte1y)
        if self.game.player_turn.carte2 == None:
            self.opulence_carte2 = self.game.p1_maine_carte.carte_none
        else:
            self.opulence_carte2 = self.game.player_turn.carte2.img
        self.opulence_carte2_rect = self.opulence_carte2.get_rect()
        self.opulence_carte2_rect.center = (self.game.player_turn.pcarte2x, self.game.player_turn.pcarte2y)
        if self.game.player_turn.carte3 == None:
            self.opulence_carte3 = self.game.p1_maine_carte.carte_none
        else:
            self.opulence_carte3 = self.game.player_turn.carte3.img
        self.opulence_carte3_rect = self.opulence_carte3.get_rect()
        self.opulence_carte3_rect.center = (self.game.player_turn.pcarte3x, self.game.player_turn.pcarte3y)

    def display_opulence_cartes(self):
        self.run_display = True
        self.no_option = True
        self.opulence_cartes()
        while self.run_display:
            self.game.display.blit(self.game.p1_maine_carte.background, (0,0))
            self.check_events_opulence_carte()
            self.game.display.blit(self.opulence_carte1, self.opulence_carte1_rect)
            self.game.display.blit(self.opulence_carte2, self.opulence_carte2_rect)
            self.game.display.blit(self.opulence_carte3, self.opulence_carte3_rect)
            self.game.update_screen()

    def check_events_opulence_carte(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                if self.opulence_carte1_rect.collidepoint(pygame.mouse.get_pos()):
                    self.game.carte_use = "carte1"
                    if self.game.player_turn.carte1.type == "Argent":
                        self.game.player_turn.jauge_de_confiance += 30
                    elif self.game.player_turn.carte1.type == "Bronze":
                        self.game.player_turn.jauge_de_confiance += 20
                    elif self.game.player_turn.carte1.type == "Acier":
                        self.game.player_turn.jauge_de_confiance += 10
                    self.run_display = False
                if self.opulence_carte2_rect.collidepoint(pygame.mouse.get_pos()):
                    self.game.carte_use = "carte2"
                    if self.game.player_turn.carte2.type == "Argent":
                        self.game.player_turn.jauge_de_confiance += 30
                    elif self.game.player_turn.carte2.type == "Bronze":
                        self.game.player_turn.jauge_de_confiance += 20
                    elif self.game.player_turn.carte2.type == "Acier":
                        self.game.player_turn.jauge_de_confiance += 10
                    self.run_display = False
                if self.opulence_carte3_rect.collidepoint(pygame.mouse.get_pos()):
                    self.game.carte_use = "carte3"
                    if self.game.player_turn.carte3.type == "Argent":
                        self.game.player_turn.jauge_de_confiance += 30
                    elif self.game.player_turn.carte3.type == "Bronze":
                        self.game.player_turn.jauge_de_confiance += 20
                    elif self.game.player_turn.carte3.type == "Acier":
                        self.game.player_turn.jauge_de_confiance += 10
                    self.run_display = False

    def effect_carte(self):
        self.carte_use()
        if self.game.player_turn.carte1 == None and self.game.player_turn.carte2 == None and self.game.player_turn.carte3 == None:
            pass
        else:
            self.display_opulence_cartes()
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Hautes_relations(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/hautes_relation.png")


    def effect_carte(self):
        if self.game.list_crowd.change_crowd:
            self.game.list_crowd.charge_crowd()
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Mepris_du_fortune(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/mepris_du_fortune.png")

    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Pot_de_vin(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/pot_de_vin.png")


    def effect_carte(self):
        if self.game.player_not_turn.antie_vol == False:
            if self.game.player_not_turn.caractere.classe_sociale == "populaire":
                self.game.player_not_turn.jauge_de_confiance -= 10
                self.game.player_turn.jauge_de_confiance += 10
            elif self.game.player_not_turn.caractere.classe_sociale == "noble":
                self.game.player_not_turn.jauge_de_confiance -= 5
                self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

#Populaire
class Solidarite(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/solidarite.png")


    def effect_carte(self):
        self.game.player_turn.jauge_de_confiance += 15
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Priere_misericordieuse(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/priere_misericordieuse.png")


    def effect_carte(self):
        chance = random.randint(1, 2)
        if self.game.player_turn.carte_chance:
            self.game.player_turn.jauge_de_confiance += 20
        elif chance == 1:
            self.game.player_turn.jauge_de_confiance += 20
            self.carte_use()
        elif chance == 2:
            self.game.player_turn.jauge_de_confiance -= 5
            self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Coup_de_chance(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/coup_de_chance.png")


    def effect_carte(self):
        self.game.player_turn.carte_chance = True
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()

class Avantage_du_nombre(Cartes):
    def __init__(self, game,  name, type):
        Cartes.__init__(self, game,  name, type)
        self.img = pygame.image.load("assets/cartes/avantage_du_nombre.png")


    def effect_carte(self):
        if self.game.player_not_turn.antie_vol == False:
            if self.game.player_not_turn.caractere.classe_sociale == "noble":
                self.game.player_not_turn.jauge_de_confiance -= 10
                self.game.player_turn.jauge_de_confiance += 10
            elif self.game.player_not_turn.caractere.classe_sociale == "populaire":
                self.game.player_not_turn.jauge_de_confiance -= 5
                self.game.player_turn.jauge_de_confiance += 5
        self.carte_use()
        if self.game.player_turn.play_two != True:
            self.game.end_turn()
