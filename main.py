import sys, pygame
import random
from random import randrange
from classes import Player
from classes import Labobject
from classes import Guardian
pygame.init()


# Screen creation:
screen = pygame.display.set_mode((300, 300))
# Picture of the walls:
wall = pygame.image.load('floor-tiles-20x20.png').convert()


# x = 15
# y = 15
# labyrinth = [['']*y for _ in range(x)]
# print(labyrinth)
labyrinth = [
    ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['D', 'P', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', 'G', 'A'],
    ['m', '', '', '', '', '', '', '', '', '', '', '', '', '', 'm'],
    ['m', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm', 'm']]


def draw_labyrinth(lab, l_wall, l_none):
    x = 0
    for row in lab:
        y = 0
        for column in row:
            if column == 'm':
                screen.blit(wall, (x*20, y*20), (100, 0, 20, 20))
                l_wall.append(screen.blit(wall, (x*20, y*20), (100, 0, 20, 20)))
            if column == '':
                screen.blit(wall, (x*20, y*20), (380, 0, 20, 20))
                l_none.append(screen.blit(wall, (x*20, y*20), (380, 0, 20, 20)))
            if column == 'D':
                screen.blit(wall, (x*20, y*20), (160, 20, 20, 20))
            if column == 'A':
                screen.blit(wall, (x*20, y*20), (160, 20, 20, 20))
            y += 1
        x += 1


def draw_people(lab, lettre, classe):
    x = 0
    for row in lab:
        y = 0
        for column in row:
            if column == lettre:
                o = classe((x * 20, y * 20))
                return o
            y += 1
        x += 1


list_walls = []
list_none = []
draw_labyrinth(labyrinth, list_walls, list_none)
player = draw_people(labyrinth, "P", Player)
guardian = draw_people(labyrinth, "G", Guardian)
ether = Labobject('ether.png', list_none)
needle = Labobject('aiguille.png', list_none)

def main():
    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            draw_labyrinth(labyrinth, list_walls, list_none)
            guardian.draw_me()
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

            if player.pos.colliderect(ether.draw_me()):
                player.obj1 = True
                ether.erase_me()

            if player.pos.colliderect(needle.draw_me()):
                player.obj2 = True
                needle.erase_me()

            if player.pos.collidelist(list_walls) != -1:
                player.pos.x = old_posx
                player.pos.y = old_posy

            if player.pos.colliderect(guardian.draw_me()):
                if player.obj1 is True and player.obj2 is True:
                    print("YOU WIN")
                    guardian.erase_me()
                    player.pos.y = guardian.pos.y + 20
                    return "CONGRATULATION"
                else:
                    print("YOU LOOSE")
                    return "GAME OVER"
            player.draw_me()

        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
