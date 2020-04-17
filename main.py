#!/usr/bin/python3
# -*-coding: utf8 -*-

import sys
import pygame
import time
from class_labyrinth import Lab
from class_player import Player
from class_guardian import Guardian
from class_object import Labobject
from fonction import create_character, erase_pos_character, erase_pos_object


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
    erase_pos_object(labyrinth.l_none, ether)
    needle = Labobject('aiguille.png', labyrinth.l_none, screengame)
    erase_pos_object(labyrinth.l_none, needle)
    pipe = Labobject('tube_plastique.png', labyrinth.l_none, screengame)
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
                if player.obj1 is True and player.obj2 is True and player.obj3 is True:
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


if __name__ == "__main__":
    main()
