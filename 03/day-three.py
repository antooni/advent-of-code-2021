import os
path = os.path.abspath('./input.txt')

bitsBalances = [0,0,0,0,0,0,0,0,0,0,0,0]

def trimLastCharacter(string):
    return string[0:len(string)-1]

with open(path) as f:
    for line in f:
        for i, character in enumerate(trimLastCharacter(line)):
            if(character == '0'):
                bitsBalances[i] -= 1
                continue
            if(character == '1'):
                bitsBalances[i] += 1

gammaString = '0b'
epsilonString = '0b'

for balance in bitsBalances:
    if(balance >= 0):
        gammaString += '1'
        epsilonString += '0'
        continue

    if(balance < 0):
        gammaString += '0'
        epsilonString += '1'

print('\ngamma = ', gammaString)
print('epsilon = ', epsilonString)
print('\npower consumption = ',int(gammaString,2) * int(epsilonString,2))

# part 2

def findMatching(bitNumber,array, filter):
    if(len(array) == 1): 
        return '0b'+array[0]
    
    balance = 0
    for line in array:
        if(line[bitNumber] == '1'):
            balance += 1
            continue
        if(line[bitNumber] == '0'):
            balance -= 1
            
    bitValue = filter[0] if balance >= 0 else filter[1]

    result = []
    for line in array:
        if(line[bitNumber] == bitValue):
            result.append(line)

    return findMatching(bitNumber+1, result, filter)


lines = open(path).readlines()

oxygenGenerator = findMatching(0,lines, '10')
co2Scrubber = findMatching(0,lines, '01')

print('\noxygen generator rating = ',trimLastCharacter(oxygenGenerator))
print('co2 scrubber rating = ', trimLastCharacter(co2Scrubber))

print('\nlife support rating = ', int(oxygenGenerator,2) * int(co2Scrubber,2))





