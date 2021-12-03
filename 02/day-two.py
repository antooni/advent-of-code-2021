import os
path = os.path.abspath('./input.txt')

class Coordinates:
    def __init__(self, x, y, aim):
        self.x = x
        self.y = y
        self.aim = aim


def moveForward(cords: Coordinates, value) :
    cords.x += value
    cords.y += cords.aim * value
    return cords


def moveUp(cords, value) :
    cords.aim -= value
    return cords


def moveDown(cords, value) :
    cords.aim += value
    return cords

dict = {
    "forward": moveForward,
    "up":moveUp,
    "down":moveDown,
}


def getDirection(line):
    return line.split(' ')[0]

def getValue(line):
    return int(line.split(' ')[1])

with open(path) as f:
    cords = Coordinates(0,0,0)
    for line in f:
        cords = dict[getDirection(line)](cords, getValue(line))

    print('x = ', cords.x)
    print('y = ', cords.y)
    print('multiplied = ', cords.x * cords.y)
