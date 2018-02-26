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
        self.image_pack = ["data/left.png", "data/right.png"]
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).convert_alpha()
            i = []
            i.append(temp.subsurface(0, 0, 47, 85))
            i.append(temp.subsurface(47, 0, 134, 85))
            i.append(temp.subsurface(134, 0, 210, 85))
            self.images.append(i)
            print("Done")
        self.moving = [0, 0, 0, 0]

    def move(self):
        if self.moving[0] == 1:
            self.x += PLAYER_SPEED
            self.direction = RIGHT
        if self.moving[1] == 1:
            self.y += PLAYER_SPEED
        if self.moving[2] == 1:
            self.x -= PLAYER_SPEED
            self.direction = LEFT
        if self.moving[3] == 1:
            self.y -= PLAYER_SPEED

        if self.x <= 0: self.x = 0
        if self.y <= 0: self.y = 0
        if self.x >= SCREEN_WIDTH - 22: self.x = SCREEN_WIDTH - 22
        if self.y >= SCREEN_HEIGHT - 41: self.y = SCREEN_HEIGHT - 41

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        pass
