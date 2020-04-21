#!/usr/bin/python3
# -*-coding: utf8 -*-

import pygame
import os


class Lab:
    """Labyrinth Class."""

    def __init__(self, file, screen):
        """Constructor of this class.

        Parameters :

        :param file : a file of the labyrinth configuration.
        :type file : file
        :param screen : the game screen.
        :type screen : pygame surface.

        The constructor create a labyrinth with an image for each element,
        a wall list, a list of empty positions and a configuration.
        """
        self.screen = screen
        self.fichier = file
        self.l_wall = []
        self.l_none = []
        self.config = []
        self.wall = pygame.image.load(os.path.join('image', 'wall.png'))\
            .convert()

    def generate_lab(self):
        """
        Generate the labyrinth configuration from file,
        add the wall positions to the wall list and
        the empty positions to the empty position.
        """

        with open(self.fichier, "r") as fichier:
            x = 0
            for row in fichier:
                row_lab = []
                y = 0
                for lettre in row:
                    if lettre != '\n':
                        row_lab.append(lettre)
                    if lettre == 'm':
                        self.l_wall.append((x*20, y*20, 20, 20))
                    if lettre == 'x':
                        self.l_none.append((x*20, y*20, 20, 20))
                    y += 1
                x += 1
                self.config.append(row_lab)

    def display_lab(self):
        """
        Diplay the image for each elements of the labyrinth
        in the game screen.
        """

        x = 0
        for row in self.config:
            y = 0
            for column in row:
                if column == 'm':
                    self.screen.blit(self.wall, (x*20, y*20),
                                     (100, 0, 20, 20))
                if column == 'x':
                    self.screen.blit(self.wall, (x*20, y*20),
                                     (380, 0, 20, 20))
                if column == 'D':
                    self.screen.blit(self.wall, (x*20, y*20),
                                     (160, 20, 20, 20))
                if column == 'A':
                    self.screen.blit(self.wall, (x*20, y*20),
                                     (160, 20, 20, 20))
                y += 1
            x += 1
