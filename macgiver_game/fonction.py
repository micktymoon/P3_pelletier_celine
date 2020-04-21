#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import time
from classes.class_labyrinth import Lab
from classes.class_player import Player
from classes.class_guardian import Guardian
from classes.class_object import Labobject


def create_character(labconfig, lettre, class_char, screen1):
    """
    Create a character on the labyrinth.

    Parameters:

     :param labconfig : the labyrinth configuration.
     :type labconfig : list.
     :param lettre : the lettre of the character we want to create.
     :type lettre : str.
     :param class_char : the character's classe.
     :type class_char : class.
     :param screen1 : the game screen.
     :type screen1 : pygame surface.

    This function create a character in the labyrinth configuration,
    using his letter in the configuration and his class.

     Returns:

     :return: the character in the game screen.
     :rtype: class object.
    """
    i = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                o = class_char((i * 20), (y * 20), screen1)
                return o
            y += 1
        i += 1


def erase_pos_character(labconfig, lettre):
    """
    Change the character's lettre to a "x" in the labyrinth's configuration.

    Parameters:

    :param labconfig : the labyrinth configuration.
    :type labconfig : list.
    :param lettre : the lettre of the character we want to create.
    :type lettre : str.

    This function replace the character's letter in the labyrinth
    configuration with a 'x', this indicates an empty position.

    Returns:

    :return: the labyrinth configuration.
    :rtype: list.
    """
    i = 0
    for row in labconfig:
        y = 0
        for column in row:
            if column == lettre:
                row[y] = 'x'
                return labconfig
            y += 1
        i += 1


def erase_pos_object(list_none, object_lab):
    """Erase the object position from the list of the empty position

    Parameters:

    :param list_none : empty labyrinth position list.
    :type list_none : list.
    :param object_lab : labyrinth object.
    :type : Lab_object object.

    This function delete the position of the object in the list given as a
    parameter, to prevent multiple objects from being in the same position.
    """
    for x in list_none:
        if x == object_lab:
            del list_none[x]


def main():
    """Run the game."""
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
    erase_pos_object(labyrinth.l_none, ether)
    needle = Labobject('aiguille.png', labyrinth.l_none, screengame)
    erase_pos_object(labyrinth.l_none, needle)
    pipe = Labobject('tube.png', labyrinth.l_none, screengame)
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

            if player.pos.colliderect(pipe.pos):
                player.obj3 = True

            if player.pos.collidelist(labyrinth.l_wall) != -1:
                player.pos.x = old_posx
                player.pos.y = old_posy

            if player.pos.colliderect(guardian.my_rect()):
                if player.obj1 and player.obj2 and player.obj3 is True:
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
        if player.obj3 is False:
            pipe.draw_me()
        guardian.draw_me()
        player.draw_me()
        pygame.display.flip()
