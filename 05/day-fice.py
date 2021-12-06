from pathlib import Path
import numpy as np
import math

path = Path(__file__).resolve().parents[0].joinpath('input.txt')

array = np.zeros((1000,1000))

with open(path) as f:
    line = f.readline()
    while line:
        arr = line.strip('\n').split(' -> ')
        p1 = arr[0].split(',')
        p2 = arr[1].split(',')
        if(p1[0] == p2[0]):
            x = int(p1[0])
            y = 0
            start = min(int(p1[1]), int(p2[1]))
            end = max(int(p1[1]), int(p2[1])) + 1
            
            for y in range(start, end):
                array[y][x] += 1
            
        if(p1[1] == p2[1]):
            y = int(p2[1])
            x = 0
            start = min(int(p1[0]), int(p2[0]))
            end = max(int(p1[0]), int(p2[0])) + 1 
           
            for x in range(start, end):
                array[y][x] += 1
                
        if(abs(int(p1[0]) - int(p2[0])) == abs(int(p1[1]) - int(p2[1]))):
            print('diagonal')
            print(arr)
            
            x = int(p1[0])
            y = int(p1[1])            
            span = abs(int(p1[0]) - int(p2[0]))
            
            for i in range(span+1):
                array[y][x] += 1
                print(array[y][x])
                if(int(p1[0]) < int(p2[0])):
                    x += 1
                else:
                    x -= 1
                if(int(p1[1]) < int(p2[1])):
                    y += 1
                else:
                    y -= 1
            
           
        line = f.readline()

print(array)
print(np.count_nonzero(array > 1))