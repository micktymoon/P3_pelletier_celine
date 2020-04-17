#!/usr/bin/python3
# -*-coding: utf8 -*-
import pygame


class Guardian(pygame.sprite.Sprite):
    """Class for the labyrinth guardian."""

    def __init__(self, x, y, screen):
        """Constructor of this class"""
        super(Guardian, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('Gardien.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = self.rect.move(x, y)

    def draw_me(self):
        """Display the guardian image."""

        self.screen.blit(self.image, self.pos)

    def my_rect(self):
        """Return the rectangle of the guardian."""

        return self.x, self.y, 20, 20
