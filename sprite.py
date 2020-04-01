#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import random

pygame.init()

# Screen creation:
screen = pygame.display.set_mode((300, 300))


class Player(pygame.sprite.Sprite):
    """Player Class."""

    def __init__(self, x, y):
        """Constructor of this class."""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('MacGyver.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.speed_right = [20, 0]
        self.speed_left = [-20, 0]
        self.speed_up = [0, -20]
        self.speed_down = [0, 20]
        self.pos = self.rect.move((x, y))
        self.x = x
        self.y = y
        self.obj1 = False
        self.obj2 = False

    def move_right(self):
        """Move the player on the right."""

        self.pos = self.pos.move(self.speed_right)
        if self.pos.right >= 280:
            self.pos.right = 280

    def move_left(self):
        """Move the player on the left."""

        self.pos = self.pos.move(self.speed_left)
        if self.pos.left <= 0:
            self.pos.left = 20

    def move_up(self):
        """Move the player on the top."""

        self.pos = self.pos.move(self.speed_up)
        if self.pos.top <= 0:
            self.pos.top = 20

    def move_down(self):
        """Move the player on the bottom."""

        self.pos = self.pos.move(self.speed_down)
        if self.pos.bottom >= 280:
            self.pos.bottom = 280

    def draw_me(self):
        """Draw player."""

        screen.blit(self.image, self.pos)


class Labobject(pygame.sprite.Sprite):
    """Class for labyrinth objects."""

    def __init__(self, image, list):
        """Constructor of this class"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = random.choice(list)

    def draw_me(self):
        """Display the object image."""

        screen.blit(self.image, self.pos)


class Guardian(pygame.sprite.Sprite):
    """Class for the labyrinth guardian."""

    def __init__(self, x, y):
        """Constructor of this class"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Gardien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = self.rect.move(self.x, self.y)

    def draw_me(self):
        """Display the guardian image."""

        screen.blit(self.image, self.pos)

    def my_rect(self):
        """Return the rectangle of the guardian."""

        return self.x, self.y, 20, 20
