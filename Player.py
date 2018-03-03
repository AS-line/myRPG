# coding: utf-8

import pygame
from Constants import *


class Player():
    def __init__(self, name):
        self.state = ALIVE
        self.direction = RIGHT
        self.x = START_X
        self.y = START_Y
        self.name = name
        self.hp = MAX_HP
        self.mp = MAX_MP
        self.image_pack = ["data/right.png", "data/down.png", "data/left.png",
                           "data/up.png"]
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = [temp.subsurface(0, 0, 64, 64), temp.subsurface(64, 0, 64, 64), temp.subsurface(128, 0, 64, 64)]
            self.images.append(i)
            print("Done")
        self.moving = [0, 0, 0, 0]

    def move(self):
        if self.moving[RIGHT] == 1:
            self.x += PLAYER_SPEED
            self.direction = RIGHT
        if self.moving[DOWN] == 1:
            self.y += PLAYER_SPEED
            self.direction = DOWN
        if self.moving[LEFT] == 1:
            self.x -= PLAYER_SPEED
            self.direction = LEFT
        if self.moving[UP] == 1:
            self.y -= PLAYER_SPEED
            self.direction = UP

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH - 60: self.x = SCREEN_WIDTH - 60

        if self.y >= SCREEN_HEIGHT - 70: self.y = SCREEN_HEIGHT - 70

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(pygame.image.load("data/hpframe.png").convert_alpha(), (self.x+12, self.y + 58))
        screen.blit(pygame.image.load("data/mpframe.png").convert_alpha(), (self.x+12, self.y + 58 + 6))
        m = 1
        z = self.hp // 5
        while m <= z:
            screen.blit(pygame.image.load("data/hptick.png"), (self.x +11+m*2, self.y + 59))
            m += 1
        m = 1
        z = self.mp // 5
        while m <= z:
            screen.blit(pygame.image.load("data/mptick.png"), (self.x+11+m*2, self.y + 59+6))
            m += 1

    def tick(self):
        if self.mp < MAX_MP:
            self.mp += MP_REG
        if self.hp < MAX_HP:
            self.hp += HP_REG
