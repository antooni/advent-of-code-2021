from pathlib import Path
import numpy as np
  
CROSSED = -1
  
def main():
    path = Path(__file__).resolve().parents[0].joinpath('example.txt')

#PART 1
    draw = get_draw(path)
    cards = get_cards(path)
        
    won = False
    for d in draw:
        for i, card in enumerate(cards):
            card = cross_number(card, d)
            
            if(is_row_winning(card) or is_column_winning(card)):
                won = True
                result = sum_up_card(card) * d
                print('BINGO!!! result =',result)
                break
                
        if(won):
            break           
# PART 2
    draw = get_draw(path)
    cards = get_cards(path)
      
    won_ids = set(())
    
    for d in draw:
        for i, card in enumerate(cards):
            card = cross_number(card, d)
            
            if(is_row_winning(card) or is_column_winning(card)):
                won_ids.add(i)
                
                if(len(cards) == len(won_ids)):
                    result = sum_up_card(card) * d
                    print('BINGO!!! result =',result)
                    break

        if(len(cards) == len(won_ids)):
            break
            
def sum_up_card(card):
    card[card == CROSSED] = 0
    return np.sum(card)

def cross_number(card, number):
    card[card == number] = CROSSED
    return np.array(card).reshape(5,5)
    
def is_row_winning(card):
    for x in card:
        isWinning = True
        for y in x:
            if(y != CROSSED):
                isWinning = False
        if(isWinning):
            return True
    return False

def is_column_winning(card):    
    for col in range(card.shape[1]):
        isWinning = True
        for y in card[:,col]:
            if y != CROSSED:
                isWinning = False
        if(isWinning):
            return True
    return False    

def get_draw(path):
    return [int(x) for x in open(path).readline().strip('\n').split(',')]

def get_cards(path):
    cards = []
    with open(path) as f:
        f.readline()
        while f.readline():
            card = []
            for i in range(5):
                card.extend([int(x) for x in f.readline().strip('\n').split(' ') if x != ''])
            cards.append(np.array(card).reshape(5,5))
        return cards

                            
if __name__ == '__main__':
    main()