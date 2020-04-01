#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import random

pygame.init()

# Screen creation:
screen = pygame.display.set_mode((300, 300))


class Lab:
    """Labyrinth Class."""

    def __init__(self, fichier):
        """Constructor of this class"""
        self.fichier = fichier
        self.lab = []
        self.l_wall = []
        self.l_none = []
        self.config = 0
        self.wall = pygame.image.load('floor-tiles-20x20.png').convert()

    def generate_lab(self):
        """Generate the labyrinth"""

        with open(self.fichier, "r") as fichier:
            config = []
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
                config.append(row_lab)
            self.config = config

    def display_lab(self):
        """Diplay the labyrinth, add rectangles of walls to l_wall and blacks rectangles to the l_none"""

        x = 0
        for row in self.config:
            y = 0
            for column in row:
                if column == 'm':
                    screen.blit(self.wall, (x * 20, y * 20), (100, 0, 20, 20))
                if column == 'x':
                    screen.blit(self.wall, (x * 20, y * 20), (380, 0, 20, 20))
                if column == 'D':
                    screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                if column == 'A':
                    screen.blit(self.wall, (x * 20, y * 20), (160, 20, 20, 20))
                y += 1
            x += 1


