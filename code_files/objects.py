import random
import math
import numpy as np
import pygame
import os

SCREEN_WIDTH=1280
SCREEN_HEIGHT=720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 素数クラス
class Prime():
    def return_list(n):
        prime_list=np.array([2,3])
        c=5
        while len(prime_list)<n:
            pl=prime_list[:np.max(np.where(prime_list<=math.sqrt(c)))+1]
            for i in pl:
                if c%i==0:
                    break
            else:
                prime_list=np.append(prime_list,c)
            c+=1
        prime_list=prime_list.tolist()
        target_list=[1,1,1]
        target_prime_list=[[1],[1],[1]]
        pl=prime_list.copy()
        for i in range(len(pl)):
            prime=random.choice(pl)
            n=random.randint(0,2)
            target_list[n]*=prime
            target_prime_list[n].append(prime)
            pl.remove(prime)
        for tp in target_prime_list:
            tp=tp.sort()
        return target_list,target_prime_list,prime_list

#共通クラス
class Objects(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, vy, number, prime, position):
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        self.x=x
        self.y=y
        self.vy=vy
        self.num=number
        self.primes=prime
        self.pos=position

    def go_right(self):
        if self.pos==2:
            self.pos=0
        else:
            self.pos+=1
    
    def go_left(self):
        if self.pos==0:
            self.pos=2
        else:
            self.pos-=1

    def drs1(self,screen):
        screen.blit(self.png, (self.x,self.y))

    def drs2(self,screen):
        screen.blit(self.png, (self.x[self.pos],self.y))
 
# 的クラス
class Target(Objects):
    def __init__(self, position, x, y, number, prime):
        super().__init__(screen, x, y, None, number, prime, position)
        self.img1_path = os.getcwd().replace(chr(92), '/')
        self.png = pygame.image.load(self.img1_path + "/img/target.png")
        self.image = pygame.Surface((400, 300))
    
    def text(self,screen):
        self.len_num = int(math.log10(self.num) + 1)
        self.fs = int(125 - 17 * math.log2(self.len_num))
        font = pygame.font.SysFont("Bebas Neue Regular", self.fs)
        text = font.render(str(self.num), True, (62,77,102))
        text_rect = text.get_rect(center=(self.x+200,self.y+150))
        screen.blit(text, text_rect)
    
    def judge(self, z):
        if self.num % z == 0:
            self.num /= z
            self.num = int(self.num)
            return True
        else:
            self.num *= z
            return False
    
#バレットクラス
class Bullet(Objects):
    def __init__(self, x, y, vy, number, position):
        super().__init__(screen, x, y, vy, number, None, position)
        self.pp=0
        self.img2_path = os.getcwd().replace(chr(92), '/')
        self.png = pygame.image.load(self.img2_path + "/img/bullet.png")
        self.image = pygame.Surface((200, 200))
    
    def move(self):
        self.y += self.vy
    
    def text(self,screen):
        font1 = pygame.font.SysFont("Bebas Neue Regular", 100)
        text = font1.render(str(self.num[self.pp]), True, (62,77,102))
        text_rect = text.get_rect(center=(self.x[self.pos]+150,self.y+150))
        screen.blit(text, text_rect)
        font2 = pygame.font.SysFont("Bebas Neue Regular", 35)
        tee = font2.render("NEXT PRIME :", True, (62,77,102))
        tee_rect = tee.get_rect(center=(250,650))
        screen.blit(tee, tee_rect)
        for i in range(len(self.num)):
            if i != self.pp:
                tn = font2.render(str(self.num[i]), True, (62,77,102))
            elif i == self.pp:
                tn = font2.render(str(self.num[i]), True, "RED")
            tn_rect = tn.get_rect(center=(350+40*i,650))
            screen.blit(tn, tn_rect)


#プレイヤークラス
class Player(Objects):
    def __init__(self, x, y, position):
        super().__init__(screen, x, y, None, None, None, position)
        self.img3_path = os.getcwd().replace(chr(92), '/')
        self.png_path = str(self.img3_path) + "/img/player.png"
        self.png=pygame.image.load(self.png_path)
        self.image=pygame.Surface((200, 200))

#音楽クラス
class Music():
    def __init__(self):
        pygame.mixer.init(frequency = 44100)
        pygame.mixer.music.set_volume(0.45)
        self.music1_path = os.getcwd().replace(chr(92), '/')
    def title_music(self):
        pygame.mixer.music.load(self.music1_path + "/bgm/the-sound-of-water-and.ogg")
        pygame.mixer.music.play(-1)
    
    def game_music(self):
        pygame.mixer.music.load(self.music1_path + "/bgm/Step Into Infinity.ogg")
        pygame.mixer.music.play(-1)

    def score_music(self):
        pygame.mixer.music.load(self.music1_path + "/bgm/epic-cinematic.ogg")
        pygame.mixer.music.play(-1)
    
    def music_stop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.fadeout(1000)

#効果音クラス
class SE():
    def __init__(self):
        pygame.mixer.init(frequency = 44100)
        self.SE1_path = os.getcwd().replace(chr(92), '/')
        self.tc=pygame.mixer.Sound(self.SE1_path + "/SE/button63.ogg")
        self.te=pygame.mixer.Sound(self.SE1_path + "/SE/button09.ogg")
        self.gc=pygame.mixer.Sound(self.SE1_path + "/SE/button55.ogg")
        self.ge=pygame.mixer.Sound(self.SE1_path + "/SE/magic04.ogg")
        self.gO=pygame.mixer.Sound(self.SE1_path + "/SE/button01.ogg")
        self.gN=pygame.mixer.Sound(self.SE1_path + "/SE/button56.ogg")
    
    def title_cursor(self):
        self.tc.play()
        self.tc.set_volume(0.5)
    
    def title_enter(self):
        self.te.play()
        self.te.set_volume(0.5)
    
    def game_cursor(self):
        self.gc.play()
        self.gc.set_volume(0.5)
    
    def game_enter(self):
        self.ge.play()
        self.ge.set_volume(0.5)
    
    def game_OK(self):
        self.gO.play()
        self.gO.set_volume(0.5)
    
    def game_NG(self):
        self.gN.play()
        self.gN.set_volume(0.5)