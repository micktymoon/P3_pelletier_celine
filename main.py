#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import random
from random import randrange
from world import*
from sprite import*

pygame.init()

# Screen creation:
screen = pygame.display.set_mode((300, 300))
# Picture of the walls:
wall = pygame.image.load('floor-tiles-20x20.png').convert()
# generate and diplay the labyrinth:
labyrinth = Lab('labyrinth')
labyrinth.generate_lab()
labyrinth.display_lab()


def draw_character(labconfig, lettre, classe):
    """
    draw a character on the labyrinth
    """
    x = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                o = classe((x*20), (y*20))
                return o
            y += 1
        x += 1


def erase_pos_character(labconfig, lettre):
    """
    change the lettre of the character to a "x" in the configuration of the labyrinth.
    """
    x = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                row[y] = "x"
                return labconfig
            y += 1
        x += 1


# draw the characters and the objects on the labyrinth:
player = draw_character(labyrinth.config, "P", Player)
labyrinth.config = erase_pos_character(labyrinth.config, "P")
guardian = draw_character(labyrinth.config, "G", Guardian)
ether = Labobject('ether.png', labyrinth.l_none)
needle = Labobject('aiguille.png', labyrinth.l_none)


def main():

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            old_posx = player.pos.x
            old_posy = player.pos.y

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.move_up()

                if event.key == pygame.K_DOWN:
                    player.move_down()

                if event.key == pygame.K_RIGHT:
                    player.move_right()

                if event.key == pygame.K_LEFT:
                    player.move_left()

            if player.pos.colliderect(ether.my_rect()):
                player.obj1 = True

            if player.pos.colliderect(needle.my_rect()):
                player.obj2 = True

            if player.pos.collidelist(labyrinth.l_wall) != -1:
                player.pos.x = old_posx
                player.pos.y = old_posy

            if player.pos.colliderect(guardian.my_rect()):
                if player.obj1 is True and player.obj2 is True:
                    player.pos.y = guardian.pos.y + 20
                    print("YOU WIN")
                    sys.exit()

                else:
                    print("YOU LOOSE")
                    sys.exit()

        labyrinth.display_lab()
        if player.obj1 is False:
            ether.draw_me()
        if player.obj2 is False:
            needle.draw_me()
        guardian.draw_me()
        player.draw_me()
        pygame.display.flip()


if __name__ == "__main__":
    main()
