#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import time
from world import Lab
from sprite import Labobject, Guardian, Player


def create_character(labconfig, lettre, classe, screen1):
    """Draw a character on the labyrinth."""
    i = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                o = classe((i*20), (y*20), screen1)
                return o
            y += 1
        i += 1


def erase_pos_character(labconfig, lettre):
    """Change the lettre to a "x" in the configuration of the labyrinth."""
    i = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                row[y] = 'x'
                return labconfig
            y += 1
        i += 1


def main():

    pygame.init()
    # Screen creation:
    screengame = pygame.display.set_mode((300, 300))
    # Generate and diplay the labyrinth:
    labyrinth = Lab('labyrinth', screengame)
    labyrinth.generate_lab()
    # Draw the characters and the objects on the labyrinth:
    player = create_character(labyrinth.config, "P", Player, screengame)
    guardian = create_character(labyrinth.config, "G", Guardian, screengame)
    ether = Labobject('ether.png', labyrinth.l_none, screengame)
    for x in labyrinth.l_none:
        if x == ether:
            del labyrinth.l_none[x]
    needle = Labobject('aiguille.png', labyrinth.l_none, screengame)
    erase_pos_character(labyrinth.config, "P")

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

            if player.pos.colliderect(ether.pos):
                player.obj1 = True

            if player.pos.colliderect(needle.pos):
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

        time.sleep(1/60)
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
