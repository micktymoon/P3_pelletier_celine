#!/usr/bin/python3
# -*-coding: utf8 -*-

import pygame
from macgiver_game.fonction_chemin import path_to_image


class Player(pygame.sprite.Sprite):
    """Class for the labyrinth player."""

    def __init__(self, x, y, screen):
        """
        Constructor of this class.

        Parameters:
        :param x : the character's position x on the labyrinth's
                    configuration.
        :type x : int
        :param y : the character's position y on the labyrinth's
                    configuration.
        :type y : int
        :param screen : the game screen.
        :type screen : pygame.surface.Surface

        The constructor allows you to create a Player object with an image,
        a position and 3 objects.
        """

        super(Player, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(path_to_image('MacGyver.png'))\
            .convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.pos = self.rect.move((x, y))
        self.x = x
        self.y = y
        self.obj1 = False
        self.obj2 = False
        self.obj3 = False

    def move_right(self):
        """Move the player on the right."""

        self.pos = self.pos.move([20, 0])
        if self.pos.right >= 280:
            self.pos.right = 280

    def move_left(self):
        """Move the player on the left."""

        self.pos = self.pos.move([-20, 0])
        if self.pos.left <= 0:
            self.pos.left = 20

    def move_up(self):
        """Move the player on the top."""

        self.pos = self.pos.move([0, -20])
        if self.pos.top <= 0:
            self.pos.top = 20

    def move_down(self):
        """Move the player on the bottom."""

        self.pos = self.pos.move([0, 20])
        if self.pos.bottom >= 280:
            self.pos.bottom = 280

    def draw_me(self):
        """Display the player's image on the game screen."""

        self.screen.blit(self.image, self.pos)
