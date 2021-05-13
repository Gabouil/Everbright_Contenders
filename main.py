from game import Game
import pygame

pygame.init()
g = Game()

while g.running:
    g.intro.play_intro()