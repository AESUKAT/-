import pygame
import sys

SCREEN_WIDTH=1280
SCREEN_HEIGHT=720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Manual(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()

    def text(self,screen):
        f1 = pygame.font.SysFont("hg正楷書体pro", 35)
        self.t1=["ゲームをスタートすると素数の弾が渡される",
        "素数の弾で合成数の的を撃ち割れ",
        "ただし、失敗すると的は積を得る",
        "正確なエイムで全ての合成数を'1'に返すのだ"]
        for i in range(len(self.t1)):
            tn = f1.render(self.t1[i], True, (62,77,102))
            tn_rect = tn.get_rect(center=(SCREEN_WIDTH/2,180+50*i))
            screen.blit(tn, tn_rect)
        
        self.t2=["方向キー","スペースキー","ESCキー"]
        for i in range(len(self.t2)):
            tn = f1.render(self.t2[i], True, (62,77,102))
            tn_rect = tn.get_rect(center=(SCREEN_WIDTH/2+80,500+50*i))
            screen.blit(tn, tn_rect)

        self.t3=["移動","決定&射撃","リセット"]
        for i in range(len(self.t3)):
            tn = f1.render(self.t3[i], True, (62,77,102))
            tn_rect = tn.get_rect(center=(SCREEN_WIDTH/2+320,500+50*i))
            screen.blit(tn, tn_rect)

        f2 = pygame.font.SysFont("hg正楷書体pro", 50)
        self.t4=["状況","操作"]
        for i in range(len(self.t4)):
            tn = f2.render(self.t4[i], True, (28,37,54))
            tn_rect = tn.get_rect(center=(SCREEN_WIDTH/2+200*i,120+320*i))
            screen.blit(tn, tn_rect)

        f3 = pygame.font.SysFont("hg正楷書体pro", 25)
        txet = f3.render("スペースキーでタイトルへ", True, (127,144,173))
        txet_rect = txet.get_rect(center=(SCREEN_WIDTH/2,650))
        screen.blit(txet, txet_rect)
        
        f4 = pygame.font.SysFont("Bebas Neue Regular", 25)
        self.t5=["点数の計算方法", "score：S","maxscore：13,23,53(難易度順)","各的の点数：Tn", "S = maxscore - log[3](T1+T2+T3) +1","全ての的が'1'でmaxscore"]
        for i in range(len(self.t5)):
            if i!=4:
                tn = f3.render(self.t5[i], True, (127,144,173))
            else:
                tn = f4.render(self.t5[i], True, (127,144,173))
            tn_rect = tn.get_rect(center=(300,460+30*i))
            screen.blit(tn, tn_rect)