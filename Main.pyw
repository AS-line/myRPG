# coding: utf-8


import pygame
from Constants import *
from Player import *
from pygame.locals import *


class Main():
    def __init__(self, screen):
        self.screen = screen
        self.player = Player("Aslan")
        self.backround = pygame.image.load("data/background.jpg")
        self.running = True
        self.main_loop()

    def hande_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == USEREVENT+1:
                self.player.tick()
            # Передвижение игрока
            # При нажатии на клавише DOWN
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.moving = [1, 0, 0, 0]
                if event.key == K_DOWN:
                    self.player.moving = [0, 1, 0, 0]
                if event.key == K_LEFT:
                    self.player.moving = [0, 0, 1, 0]
                if event.key == K_UP:
                    self.player.moving = [0, 0, 0, 1]
                if event.key == K_z:
                    if self.player.mp >= SKILL1_COST:
                        self.player.mp -= SKILL1_COST
                        if self.player.state != SHOOT:
                            self.player.state = SHOOT
            # При отжатии клавиш UP
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.moving[0] = 0
                if event.key == K_DOWN:
                    self.player.moving[1] = 0
                if event.key == K_LEFT:
                    self.player.moving[2] = 0
                if event.key == K_UP:
                    self.player.moving[3] = 0
                if event.key == K_z:
                    self.player.state = ALIVE

    def render(self):
        # Отрисовка всего
        self.screen.blit(self.backround, (0, 0))
        self.player.render(screen)
        self.player.render_ui(screen)
        pygame.display.flip()

    def main_loop(self):
        # Основной цикл программы
        pygame.time.set_timer(USEREVENT+1, 100)
        while self.running:
            print(self.player.mp)
            self.player.tick()
            if self.player.state != DEAD:
                self.player.move()
                self.hande_events()
            self.render()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
