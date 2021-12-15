from pathlib import Path

path = Path(__file__).resolve().parent.joinpath('input.txt')

numbers = []

def is_low_point(i, j, array):
    n_columns = len(array[i])
    m_rows = len(array)
    if i - 1 >= 0 :
        if array[i][j] >= array[i-1][j]:
            return False
    if i + 1 < m_rows :
        if array[i][j] >= array[i+1][j]:
            return False
    if j - 1 >= 0:
        if array[i][j] >= array[i][j-1]:
            return False
    if j + 1 < n_columns:
        if array[i][j] >= array[i][j+1]:
            return False
    return True
        
def move_wrapper(i,j,numbers):
    sum = 1
    numbers[i][j] = -1
    
    if i < len(numbers) - 1:
        if numbers[i+1][j] != -1:
            if numbers[i+1][j] != 9:
                sum += move_wrapper(i+1,j,numbers)
    if i > 0:
        if numbers[i-1][j] != -1:
            if numbers[i-1][j] != 9:
                sum += move_wrapper(i-1,j,numbers)
    if j < len(numbers[i]) - 1:
        if numbers[i][j+1] != -1:
            if numbers[i][j+1] != 9:
                sum += move_wrapper(i,j+1,numbers)
    if j > 0:
        if numbers[i][j-1] != -1:
            if numbers[i][j-1] != 9:
                sum += move_wrapper(i,j-1,numbers)
        
    return sum  

with open(path) as f:
    line = f.readline()
    while line:
        numbers.append([int(v) for v in line.strip('\n')])
        line = f.readline()

results = []


for i, x in enumerate(numbers):
    for j, y in enumerate(x):
        if(is_low_point(i, j, numbers)):
            print(y)
            results.append(move_wrapper(i,j,numbers))
            
    
print(sorted(results))