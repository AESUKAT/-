import pygame
import sys

SCREEN_WIDTH=1280
SCREEN_HEIGHT=720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

    def text(self, screen, score):
        font4 = pygame.font.SysFont("Bebas Neue Regular", 115)
        tttt = font4.render("SCORE", True, (62,77,102))
        tttt_rect1 = tttt.get_rect(center=(SCREEN_WIDTH/2, 260))
        font5 = pygame.font.SysFont("Bebas Neue Regular", 200)
        ttttt = font5.render(score, True, (62,77,102))
        ttttt_rect1 = ttttt.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 40))
        screen.blit(tttt, tttt_rect1)
        screen.blit(ttttt, ttttt_rect1)
    
    def return_difficult(self):
        return self.dif_n[self.pos]