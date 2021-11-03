import random
import math
import numpy as np
from objects import Prime
from objects import Target
from objects import Bullet
from objects import Player
from objects import Music
from objects import SE
import title
import manual
import score
import pygame
import sys

DIFF=["EASY", "NORMAL", "HARD","説明"]
DIFF_N=[7, 11, 19]

TARGET1_X=40
TARGET2_X=440
TARGET3_X=840
TARGET_Y=40

PLAYER_X=[90,490,890]
PLAYER_P=1
PLAYER_Y=370

BULLET_X=[90,490,890]
BULLET_P=1
BULLET_VY=-12
BULLET_Y=370

SCREEN_WIDTH=1280
SCREEN_HEIGHT=720

FPS=30

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#ゲームの実行クラス
class main():
    def __init__(self):
        pygame.display.set_caption("スペースキーで決定してね")
        self.f=1
        self.player=Player(PLAYER_X, PLAYER_Y, PLAYER_P)
        self.title=title.Title(DIFF, DIFF_N)
        self.manual=manual.Manual()
        self.Music=Music()
        self.SE=SE()
        self.music_s=False

    def run(self):
        done = False
        while True:
            for event in pygame.event.get():
                # 「閉じる」ボタンを処理する
                if event.type == pygame.QUIT: done = True

            if done: break
            clock.tick(FPS)

            if self.f==1:
                if self.music_s:
                    pass
                else:
                    self.Music.title_music()
                    self.music_s=True

                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_UP:
                            self.SE.title_cursor()
                            self.title.go_up()
                        elif ev.key == pygame.K_DOWN:
                            self.SE.title_cursor()
                            self.title.go_down()

                        if ev.key == pygame.K_SPACE:
                            if self.title.pos !=3:
                                self.f=2
                                self.n=self.title.return_difficult()

                                self.target_list,self.target_prime_list,self.prime_list=Prime.return_list(self.n)

                                self.target=pygame.sprite.Group()
                                self.target.add(Target(0, TARGET1_X, TARGET_Y, self.target_list[0], self.target_prime_list[0]))
                                self.target.add(Target(1, TARGET2_X, TARGET_Y, self.target_list[1], self.target_prime_list[1]))
                                self.target.add(Target(2, TARGET3_X, TARGET_Y, self.target_list[2], self.target_prime_list[2]))
                                self.bullet=Bullet(BULLET_X, BULLET_Y, BULLET_VY, self.prime_list, BULLET_P)
                                self.Score=score.score()

                                self.Music.music_stop()
                                self.music_s=False
                            
                            elif self.title.pos == 3:
                                self.f = 7
                                self.SE.title_enter()
                            
                self.title.text(screen)

            if self.f==2:
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_LEFT:    # 左が押されたら
                            self.SE.game_cursor()
                            self.player.go_left()
                            self.bullet.go_left()
                        elif ev.key == pygame.K_RIGHT:  # 右が押されたら
                            self.SE.game_cursor()
                            self.player.go_right()
                            self.bullet.go_right()
                        if ev.key == pygame.K_SPACE:
                            self.SE.game_enter()
                            self.f=3
            
            if self.f==3:
                if self.bullet.y>100:
                    self.bullet.move()
                elif self.bullet.y<=100:
                    self.bullet.y=BULLET_Y
                    self.f=4

            if self.f==4:
                for tar in self.target:
                    if self.bullet.pos == tar.pos:
                        self.judge=tar.judge(int(self.bullet.num[self.bullet.pp]))

                if self.judge:
                    self.SE.game_OK()
                    self.judge=None
                elif not self.judge:
                    self.SE.game_NG()
                    self.judge=None  

                if self.bullet.pp<len(self.bullet.num)-1:
                    self.bullet.pp+=1
                    self.f=2
                else:
                    self.Music.music_stop()
                    self.music_s=False
                    self.f=5

            if self.f==5:
                if self.music_s:
                    pass
                else:
                    self.Music.score_music()
                    self.music_s=True

                self.score=0

                for tar in self.target:
                    self.score += tar.num

                self.score = math.log(self.score, 3)

                if self.title.pos==0:
                    self.score = 14 - self.score
                    self.maxscore = 13
                elif self.title.pos==1:
                    self.score = 24 - self.score
                    self.maxscore = 23
                elif self.title.pos==2:
                    self.score = 54 - self.score
                    self.maxscore = 53

                self.score = '{:.3f}'.format(self.score)
                self.score_m = self.score + " / " + str(self.maxscore)
                self.Score.text(screen, self.score_m)
                self.bullet.pos=1
                self.bullet.pp=0
                self.player.pos=1

                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_SPACE:
                            self.Music.music_stop()
                            self.music_s=False
                            self.f=1

            if self.f==6:
                self.bullet.pos=1
                self.bullet.pp=0
                self.player.pos=1
                self.Music.music_stop()
                self.music_s=False
                self.f=1

            if self.f==7:
                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_SPACE:
                            self.f=1
                            self.title.return_title()

                self.manual.text(screen)

            if 2<=self.f<=4:
                for tar in self.target:
                    tar.drs1(screen)
                for tar in self.target:
                    tar.text(screen)

                self.player.drs2(screen)
                self.bullet.drs2(screen)
                self.bullet.text(screen)

                if self.music_s:
                    pass
                else:
                    self.Music.game_music()
                    self.music_s=True

                for ev in pygame.event.get():
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_ESCAPE:
                            self.f=6

            pygame.display.flip()
            screen.fill((228,233,237))

        pygame.quit()   # 画面を閉じる