from game import Game
import pygame

pygame.init()
pygame.display.set_caption("Everbright's Contenders")
icon_32x32 = pygame.image.load("assets/armoirie.png")
icon_32x32 = pygame.transform.scale(icon_32x32 , (32, 32))
pygame.display.set_icon(icon_32x32)
g = Game()

while g.running:
    # g.intro.play_intro()
    g.curr_menu.display_menu()