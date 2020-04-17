#!/usr/bin/python3
# -*-coding: utf8 -*-


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
    """Change the lettre of the character to a "x" in the configuration of the labyrinth."""
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
    """erase the position of an object from the liste of empty positions."""
    for x in list_none:
        if x == object_lab:
            del list_none[x]
