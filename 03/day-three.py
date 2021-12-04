from pathlib import Path
path = Path(__file__).resolve().parents[0].joinpath('input.txt')
print(path)


def main():
# PART 1
    bits_balances = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma_str = '0b'
    epsilon_str = '0b'
    lines = open(path).readlines()

    def trim_last_character(string):
        return string[0:len(string)-1]

    for line in lines:
        for i, character in enumerate(trim_last_character(line)):
            if(character == '0'):
                bits_balances[i] -= 1
                continue
            if(character == '1'):
                bits_balances[i] += 1

    for balance in bits_balances:
        if(balance >= 0):
            gamma_str += '1'
            epsilon_str += '0'
            continue

        if(balance < 0):
            gamma_str += '0'
            epsilon_str += '1'

    print('\ngamma = ', gamma_str)
    print('epsilon = ', epsilon_str)
    print('\npower consumption = ',int(gamma_str,2) * int(epsilon_str,2))

# PART 2
    def filter_values(bit_num, array, output):
        if(len(array) == 1): 
            return '0b' + array[0]
        
        balance = 0
        for line in array:
            if(line[bit_num] == '1'):
                balance += 1
                continue
            if(line[bit_num] == '0'):
                balance -= 1
                
        bit_value = output[0] if balance >= 0 else output[1]

        result = []
        for line in array:
            if(line[bit_num] == bit_value):
                result.append(line)

        return filter_values(bit_num+1, result, output)

    oxygen_generator = filter_values(0,lines, '10')
    co2_scrubber = filter_values(0,lines, '01')

    print('\noxygen generator rating = ',trim_last_character(oxygen_generator))
    print('co2 scrubber rating = ', trim_last_character(co2_scrubber))

    print('\nlife support rating = ', int(oxygen_generator,2) * int(co2_scrubber,2))


if __name__ == "__main__":
    main()


