import numpy as np
import math
from pathlib import Path

numbers = np.array([16,1,2,0,4,2,7,1,2,14])

path = Path(__file__).resolve().parent.joinpath('input.txt')

print(path)
numbers = [int(x) for x in open(path).readline().strip('\n').split(',')]

middle = math.floor(np.sum(numbers) / len(numbers))

print(middle)
min_sum = 99999999

for i in range(np.max(numbers)+1):
    current = i
    if True:
        sum = 0
        for n in numbers:
            distance = abs(n - current)
            sum += np.sum(np.arange(distance+1))
        if(i == 0):
            min_sum = sum
        elif sum < min_sum:
            min_sum = sum
            
print(min_sum)