from game import Game
import pygame

pygame.init()
g = Game()

while g.running:
    g.curr_menu.display_menu()


pygame.quit()