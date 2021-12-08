from pathlib import Path
import numpy as np

def main():
    path = Path(__file__).resolve().parents[0].joinpath('input.txt')
    
    numbers = [int(x) for x in open(path).readline().strip('\n').split(',')]

# PART 1
    population_80 = calc_population_size_after_n_days(numbers, 80)
    print("Population size after 80 days = ", population_80)

# PART 2
    population_256 = calc_population_size_after_n_days(numbers, 256);
    print("Population size after 256 days = ", population_256)
    
def calc_population_size_after_n_days(initial_population, n_days):
    amount_of_fish_at_stage = np.zeros(9)
    
    for fish_stage in initial_population:
        amount_of_fish_at_stage[fish_stage] += 1
    
    for i in range(n_days):
        new_borns = 0
        mothers = 0
        
        for index, s in enumerate(amount_of_fish_at_stage):
            if(index == 0):
                new_borns += s
                mothers += s
                amount_of_fish_at_stage[0] -= s
            else :
                amount_of_fish_at_stage[index] -= s
                amount_of_fish_at_stage[index-1] += s
                
        amount_of_fish_at_stage[8] += new_borns
        amount_of_fish_at_stage[6] += mothers
                
    return np.sum(amount_of_fish_at_stage)
    
if __name__ == '__main__':
    main()        
