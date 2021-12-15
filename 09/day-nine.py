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
    sum = 0
    sum += move(i+1,j,1,0,numbers)
    sum += move(i-1,j,-1,0,numbers)
    sum += move(i,j+1,0,1,numbers)
    sum += move(i,j-1,0,-1,numbers)
    return sum
    
def move(x,y,dirX, dirY, array):

    if x + dirX <= 0 or x + dirX >= len(array):
        return 1
    if y + dirY <= 0 or y + dirY >= len(array[x]):
        return 1
    if array[x+dirX][y+dirY] == 9:
        return 1
    return 1 + move(x + dirX, y + dirY, dirX, dirY, array)
    

with open(path) as f:
    line = f.readline()
    while line:
        numbers.append([int(v) for v in line.strip('\n')])
        line = f.readline()

results = []
sum = 0  


for i, x in enumerate(numbers):
    for j, y in enumerate(x):
        if(is_low_point(i, j, numbers)):
            print(y)
            # sum = 0
            sum += y + 1
            # sum += move(i+1,j,1,0,numbers)
            # sum += move(i-1,j,-1,0,numbers)
            # sum += move(i,j+1,0,1,numbers)
            # sum += move(i,j-1,0,-1,numbers)
            # results.append(sum)

    
print(sum)