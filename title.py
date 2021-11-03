import pygame
import sys

SCREEN_WIDTH=1280
SCREEN_HEIGHT=720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Title(pygame.sprite.Sprite):
    def __init__(self, DIFF, DIFF_N):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.dif=DIFF
        self.dif_n=DIFF_N
        self.y=[420,470,520,600,360]
        self.pos=0

    def go_down(self):
        if self.pos==3:
            self.pos=0
        else:
            self.pos+=1
    
    def go_up(self):
        if self.pos==0:
            self.pos=3
        else:
            self.pos-=1

    def text(self,screen):
        self.len_dif=len(self.dif_n)
        font1 = pygame.font.SysFont("hg正楷書体pro", 45)
        for i in range(self.len_dif+2):
            if 0<=i<=self.len_dif-1:
                if i != self.pos:
                    text1 = font1.render(self.dif[i], True, (62,77,102))
                    text2 = font1.render(str(self.dif_n[i]), True, (62,77,102))
                elif i == self.pos:
                    text1 = font1.render(self.dif[i], True, "RED")
                    text2 = font1.render(str(self.dif_n[i]), True, "RED")
                text1_rect = text1.get_rect(center=(SCREEN_WIDTH/2 - 150,self.y[i]))
                text2_rect = text2.get_rect(center=(SCREEN_WIDTH/2 + 300,self.y[i]))
            elif i == self.len_dif:
                if i != self.pos:
                    text1 = font1.render(self.dif[i], True, (62,77,102))
                elif i == self.pos:
                    text1 = font1.render(self.dif[i], True, "RED")
                text1_rect = text1.get_rect(center=(SCREEN_WIDTH/2,self.y[i]))
            else:
                text1 = font1.render("難易度", True, (62,77,102))
                text2 = font1.render("弾数", True, (62,77,102))
                text1_rect = text1.get_rect(center=(SCREEN_WIDTH/2 - 150,self.y[i]))
                text2_rect = text2.get_rect(center=(SCREEN_WIDTH/2 + 300,self.y[i]))
            if i != self.len_dif:
                screen.blit(text1, text1_rect)
                screen.blit(text2, text2_rect)
            else:
                screen.blit(text1, text1_rect)
        
        font3 = pygame.font.SysFont("Bebas Neue Regular", 150)
        tit = font3.render("PRIME HUNTER", True, (62,77,102))
        tit_rect1 = tit.get_rect(center=(SCREEN_WIDTH/2, 220))
        screen.blit(tit, tit_rect1)
    
    def return_difficult(self):
        if self.pos != 3:
            return self.dif_n[self.pos]
    
    def return_title(self):
        self.pos = 0