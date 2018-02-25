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
            # Передвижение игрока
            # При нажатии на клавише DOWN
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if event.key == K_DOWN:
                    self.player.direction = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if event.key == K_LEFT:
                    self.player.direction = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if event.key == K_UP:
                    self.player.direction = UP
                    self.player.moving = [0, 0, 0, 1]
            # При отжатии клавиш UP
            elif event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.player.moving[RIGHT] = 0
                if event.key == K_DOWN:
                    self.player.moving[DOWN] = 0
                if event.key == K_LEFT:
                    self.player.moving[LEFT] = 0
                if event.key == K_UP:
                    self.player.moving[UP] = 0

    def render(self):
        # Отрисовка всего
        self.screen.blit(self.backround, (0, 0))
        self.player.render(screen)
        pygame.display.flip()

    def main_loop(self):
        # Основной цикл программы
        while self.running == True:
            self.player.move()
            self.render()
            self.hande_events()


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)
