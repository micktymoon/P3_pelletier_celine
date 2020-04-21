#!/usr/bin/python3
# -*-coding: utf8 -*-
import pygame
import random
import os


class Labobject(pygame.sprite.Sprite):
    """Class for labyrinth objects."""

    def __init__(self, image, list_, screen):
        """Constructor of this class.

        Parameters :

        :param image : the image of the object we want to create.
        :type image : image.
        :param list_ : position list where the object can be positioned.
        :type : list.
        :param screen : the game screen.
        :type screen : pygame surface.

        The constructor create a Labobject object with an image
        and a random position.
        """
        super(Labobject, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(os.path.join('image', image))\
            .convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = random.choice(list_)

    def draw_me(self):
        """Display the object image on the game screen."""

        self.screen.blit(self.image, self.pos)
