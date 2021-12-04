from pathlib import Path
from dataclasses import dataclass

def main():
    path = Path(__file__).resolve().parents[0].joinpath('input.txt')
    @dataclass
    class Coordinates:
        x: float
        y:float
        aim:float

    def move_forward(cords: Coordinates, value) :
        print('forward')
        cords.x += value
        cords.y += cords.aim * value
        return cords


    def move_up(cords, value) :
        print('forward')

        cords.aim -= value
        return cords


    def move_down(cords, value) :
        print('forward')

        cords.aim += value
        return cords

    move_fun = {
        "forward": move_forward,
        "up":move_up,
        "down":move_down,
    }

    def get_direction(line):
        return line.split(' ')[0]

    def get_value(line):
        return int(line.split(' ')[1])

    with open(path) as f:
        cords = Coordinates(0,0,0)
        for line in f:
            direction = get_direction(line)
            step = get_value(line)
            # print(direction,' ', step)
            cords = move_fun[direction](cords, step)

        print('x = ', cords.x)
        print('y = ', cords.y)
        print('multiplied = ', cords.x * cords.y)

if __name__ == '__main__':
    main()