from pathlib import Path
import numpy as np
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
def main():
    
    path = Path(__file__).resolve().parents[0].joinpath('input.txt')
    readings = open(path).readlines()
    
    print('PART 1 = ', calc_lines_overlaps(readings,1000, False))
    print('PART 2 = ', calc_lines_overlaps(readings,1000, True))


def calc_lines_overlaps(sonar_readings, map_size, include_diagonal_flag):
    hydrothermal_vents = np.zeros((map_size, map_size))

    for coords in sonar_readings:
        points = coords.strip('\n').split(' -> ')
        p1 = Point(int(points[0].split(',')[0]), int(points[0].split(',')[1]))
        p2 = Point(int(points[1].split(',')[0]), int(points[1].split(',')[1]))
        
        if(p1.x == p2.x):
            start = min(p1.y, p2.y)
            end = max(p1.y, p2.y) + 1
            
            for y in range(start, end):
                hydrothermal_vents[y][p1.x] += 1
            
        if(p1.y == p2.y):
            start = min(p1.x, p2.x)
            end = max(p1.x, p2.x) + 1 
           
            for x in range(start, end):
                hydrothermal_vents[p1.y][x] += 1
        
        if include_diagonal_flag:      
            if(abs(p1.x - p2.x) == abs(p1.y - p2.y)):
                x = p1.x
                y = p1.y            
                line_length = abs(p1.x - p2.x) + 1
                
                for i in range(line_length):
                    hydrothermal_vents[y][x] += 1
                    
                    if(p1.x < p2.x):
                        x += 1
                    else:
                        x -= 1
                        
                    if(p1.y < p2.y):
                        y += 1
                    else:
                        y -= 1
                    
    return np.count_nonzero(hydrothermal_vents > 1)
            
           
if __name__ == '__main__':
    main()