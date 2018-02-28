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
        self.image_pack = ["data/test_texture_right.png", "data/test_texture_down.png", "data/test_texture_left.png",
                           "data/test_texture_up.png"]
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = [temp.subsurface(0, 0, 100, 100), temp.subsurface(100, 0, 100, 100), temp.subsurface(200, 0, 100, 100)]
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
        if self.x >= SCREEN_WIDTH - 47: self.x = SCREEN_WIDTH - 47

        if self.y >= SCREEN_HEIGHT - 100: self.y = SCREEN_HEIGHT - 100

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(pygame.image.load("data/hpframe_short.png").convert_alpha(), (self.x - 10, self.y + 89))
        screen.blit(pygame.image.load("data/mannaframe_short.png").convert_alpha(), (self.x - 10, self.y + 89 + 7))
        m = 1
        z = self.hp // 10
        while m <= z:
            screen.blit(pygame.image.load("data/hptick.png"), (self.x - 15 + m * 5, self.y + 90))
            m += 1
        m = 1
        z = self.mp // 10
        while m <= z:
            screen.blit(pygame.image.load("data/mannatick.png"), (self.x - 14 + m * 5, self.y + 97))
            m += 1

    def tick(self):
        if self.mp < MAX_MP:
            self.mp += MP_REG
        if self.hp < MAX_HP:
            self.hp += HP_REG
