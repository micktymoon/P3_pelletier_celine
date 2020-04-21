#!/usr/bin/python3
# -*-coding: utf8 -*-

import pygame
import os


class Guardian(pygame.sprite.Sprite):
    """Class for the labyrinth guardian."""

    def __init__(self, x, y, screen):
        """Constructor of this class.

        Parameters:
        :param x : the character's position x on the labyrinth's configuration.
        :type x : int.
        :param y : the character's position y on the labyrinth's configuration.
        :type y : int.
        :param screen : the game screen.
        :type screen : pygame surface.

        The constructor allows you to create a Guardian object with an image and a position.
        """
        super(Guardian, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join('image', 'Gardien.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.pos = self.rect.move(x, y)

    def draw_me(self):
        """Display the guardian's image on the game screen."""

        self.screen.blit(self.image, self.pos)

    def my_rect(self):
        """Return the rectangle of the guardian."""

        return self.x, self.y, 20, 20
