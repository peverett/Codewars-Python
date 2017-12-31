#!/usr/bin/python
"""Battleship field validator Kata

Write a method that takes a field for well-known board game "Battleship" as an
argument and returns true if it has a valid disposition of ships, false
otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in
the array are numbers, 0 if the cell is free and 1 if occupied by ship.

Battleship (also Battleships or Sea Battle) is a guessing game for two players.
Each player has a 10x10 grid containing several "ships" and objective is to
destroy enemy's forces by targetting individual cells on his field. The ship
occupies one or more cells in the grid. Size and number of ships may differ
from version to version. In this kata we will use Soviet/Russian version of the
game.

* Before the game begins, players set up the board and place the ships
accordingly to the following rules:
    
* There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3
destroyers (size 2) and 4 submarines (size 1). Any additional ships are not
allowed, as well as missing ships.

* Each ship must be a straight line, except for submarines, which are just
single cell.

The ship cannot overlap or be in contact with any other ship, neither by edge
nor by corner.

This is all you need to solve this kata. If you're interested in more
information about the game, visit
http://en.wikipedia.org/wiki/Battleship_(game) 
"""

import math


def outputField(field):
    """Visual field display for verification."""
    for y in range(10):
        for x in range(10):
            char = 'X' if field[y][x] else '.'
            print('{} '.format(char), end='')
        print('')

def InShip(ships, x, y):
    """Is the x, y coordinate given 'in' a found ship?"""
    coord = (x, y)
    for ship in ships:
        if coord in ship: 
            return True
    return False

def FindShip(x, y, field):
    """given a coordinate with a 1 in it, find the rest of the ship"""
    ssx = x
    sex = -1
    ssy = y
    sey = -1
    coords = [(x, y)]
    for dx in range(x+1, 10):
        if not field[y][dx]:
            sex = dx-1
            break
        else:
            coords.append((dx, y))

    if ssx==sex: 
        for dy in range(ssy+1, 10):
            if not field[dy][x]:
                sey = dy-1
                break
            else:
                coords.append((x, dy))
    print("Found ship: {}".format(coords))
    return coords

def CheckShipBoundaries(ships):
    """Check the coords around the ship to make sure no other ship is touching
    If any coord in another ship is < 2 distance away then it is touching.
    """
    ships_copy = list(ships)
    while(len(ships_copy)):        # compare each ships coords to each other
        ship = ships_copy.pop()    # ships coords.

        for acoord in ship:
            for other_ship in ships_copy:
                for bcoord in other_ship:
                    a = abs(acoord[0]-bcoord[0])  # Distance on X-axis
                    b = abs(acoord[1]-acoord[1])  # Distance on Y-axis

                    # same row or column
                    if (a==0 and b<2) or (a==0 and b<2):
                        print("Ship ({}, {}) too close to ({}, {})".format(
                            c[0], c[1], o[0], o[1]
                            ))
                        return False
                    else:
                        # distance from a to b calculated by Pythagorus.
                        if math.sqrt(x**2 + y**2) < 2:
                            print("Ship ({}, {}) too close to ({}, {})".format(
                                c[0], c[1], o[0], o[1]
                                ))
                            return False
    return True

def CheckShipCounts(ships):
    """Count all the coordinates for each ship and store the counts in a 
    dictionary. There should be 1 count of 4, 2 counts of 3, etc.
    """
    counts = dict()
    for ship in ships:
        size = len(ship)
        counts[size] = counts.get(size, 0) + 1

    print("Ship Counts: {}".format(counts))

    try: 
        if counts[4]!= 1 or counts[3]!=2 or counts[2]!=3 or counts[1]!= 4:
            return False
    except KeyError:
        return False

    return True

def validateBattlefield(field):
    """Design 
    * Find all the ships and store their coordinates in a list.
    * Check all the different ship types are present and correct.
    * Check none of the ships are too close to each other
    """
    outputField(field)
    ships = list()

    for y in range(10):
        for x in range(10):
            if field[y][x] and not InShip(ships, x, y):
                ships.append(FindShip(x, y, field))

    return CheckShipCounts(ships) and CheckShipBoundaries(ships)
