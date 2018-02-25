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
            i = []
            i.append(temp.subsurface(0, 0, 22, 41))
            print("done")
            self.images.append(i)

        self.moving = [0, 0, 0, 0]

    def move(self):
        if self.moving[RIGHT] == 1:
            self.x += PLAYER_SPEED
        if self.moving[DOWN] == 1:
            self.y += PLAYER_SPEED
        if self.moving[LEFT] == 1:
            self.x -= PLAYER_SPEED
        if self.moving[UP] == 1:
            self.y -= PLAYER_SPEED

    def render(self, screen):
        screen.blit(self.images[self.direction][self.state], (self.x, self.y))

    def render_ui(self, screen):
        pass
