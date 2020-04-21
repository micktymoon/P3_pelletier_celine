#!/usr/bin/python3
# -*-coding: utf8 -*-

import pygame
import os


class Lab:
    """Labyrinth Class."""

    def __init__(self, fichier, screen):
        """Constructor of this class"""
        self.screen = screen
        self.fichier = fichier
        self.l_wall = []
        self.l_none = []
        self.config = []
        self.wall = pygame.image.load(os.path.join('image', 'floor-tiles-20x20.png')).convert()

    def generate_lab(self):
        """Generate the labyrinth"""

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
        """Diplay the labyrinth, add rectangles of walls to l_wall and blacks rectangles to the l_none"""

        x = 0
        for row in self.config:
            y = 0
            for column in row:
                if column == 'm':
                    self.screen.blit(self.wall, (x * 20, y * 20), (100, 0, 20, 20))
                if column == 'x':
                    self.screen.blit(self.wall, (x * 20, y * 20), (380, 0, 20, 20))
                if column == 'D':
                    self.screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                if column == 'A':
                    self.screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                y += 1
            x += 1
