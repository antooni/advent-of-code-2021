from pathlib import Path
import numpy as np
from itertools import count

def main():
    
    path = Path(__file__).resolve().parent.joinpath('input.txt')

    octopuses = np.zeros((10,10), dtype=int)
    flashes = np.zeros((10,10), dtype=int)

    flash_count = count()
    
    lines = open(path).readlines()

    for i, line in enumerate(lines):
        line = line.strip('\n')
        for j, octopus in enumerate(line):
            octopuses[i][j] = int(octopus)
            
    def flash(i,j):
        octopuses[i][j] = 0
        flashes[i][j] = 1
        next(flash_count)
        #top
        if i != 0:
            octopuses[i-1][j] += 1
            if octopuses[i-1][j] > 9:
                if flashes[i-1][j] == 0:
                    flash(i-1,j)
        #bottom
        if i != len(octopuses)-1:
            octopuses[i+1][j] += 1
            if octopuses[i+1][j] > 9:
                if flashes[i+1][j] == 0:
                    flash(i+1,j)
        #left
        if j != 0:
            octopuses[i][j-1] += 1
            if octopuses[i][j-1] > 9:
                if flashes[i][j-1] == 0:
                    flash(i,j-1)
        #right
        if j != len(octopuses[i])-1:
            octopuses[i][j+1] += 1
            if octopuses[i][j+1] > 9:
                if flashes[i][j+1] == 0:
                    flash(i,j+1)
        #bottom-left
        if i != len(octopuses)-1 and j != 0:
            octopuses[i+1][j-1] += 1
            if octopuses[i+1][j-1] > 9:
                if flashes[i+1][j-1] == 0:
                    flash(i+1,j-1)
        #bottom-right
        if i != len(octopuses)-1 and j != len(octopuses[i])-1:
            octopuses[i+1][j+1] += 1
            if octopuses[i+1][j+1] > 9:
                if flashes[i+1][j+1] == 0:
                    flash(i+1,j+1)
        #top-left
        if i != 0 and j != 0:
            octopuses[i-1][j-1] += 1
            if octopuses[i-1][j-1] > 9:
                if flashes[i-1][j-1] == 0:
                    flash(i-1,j-1)
        #top-right
        if i != 0 and j != len(octopuses[i])-1:
            octopuses[i-1][j+1] += 1
            if octopuses[i-1][j+1] > 9:
                if flashes[i-1][j+1] == 0:
                    flash(i-1,j+1)
            

        
    # STEP 0   
    # print(octopuses)

    # STEPS 1 to N
    for day in range(3000):
        octopuses = octopuses + 1
        for i, row in enumerate(octopuses):
            for j, octopus in enumerate(row):
                if octopus > 9:
                    flash(i,j)
                    
        for i, row in enumerate(flashes):
            for j, f in enumerate(row):
                if f == 1 :
                    octopuses[i][j] = 0
                    
        if np.all(flashes == 1):
            print('First simultaneous flash on day:',day+1)
            break
            
        flashes = np.zeros((10,10))
        
        if day == 99:
            print('Amount of flashes after 100 days:',next(flash_count))
        
if __name__ == "__main__":
    main()