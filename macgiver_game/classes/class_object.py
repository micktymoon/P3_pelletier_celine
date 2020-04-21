#!/usr/bin/python3
# -*-coding: utf8 -*-
import pygame
import random
import os


class Labobject(pygame.sprite.Sprite):
    """Class for labyrinth objects."""

    def __init__(self, image, list, screen):
        """Constructor of this class"""
        super(Labobject, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join('image', image)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = random.choice(list)

    def draw_me(self):
        """Display the object image."""

        self.screen.blit(self.image, self.pos)
