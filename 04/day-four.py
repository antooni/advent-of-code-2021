from pathlib import Path
import numpy as np
  
def main():
    path = Path(__file__).resolve().parents[0].joinpath('input.txt')
    
    draw = get_draw(path)
    cards = get_cards(path)
        
    won = False
    for d in draw:
        for i, card in enumerate(cards):
            card[card==d] = -1
            card = np.array(card).reshape(5,5)
            cards[i] = card
            
            for x in card:
                isWinning = True
                for y in x:
                    if(y != -1):
                        isWinning = False
                if(isWinning):
                    won = True
                    card[card==-1] = 0
                    sum = np.sum(card)
                    print('WIN ',sum * d)
                    
            for col in range(card.shape[1]):
                isWinning = True
                for y in card[:,col]:
                    if y != -1:
                        isWinning = False
                if(isWinning):
                    won = True
                    card[card==-1] = 0
                    sum = np.sum(card)
                    print('WIN ',sum * d)
        if(won):
            break
        
            
# PART 2
    draw = get_draw(path)
    cards = get_cards(path)
      
    won_ids = set(())
    
    for d in draw:
        for i, card in enumerate(cards):
            card[card==d] = -1
            card = np.array(card).reshape(5,5)
            cards[i] = card
            
            won = False
            for x in card:
                isWinning = True
                for y in x:
                    if(y != -1):
                        isWinning = False
                if(isWinning):
                    if(len(cards) - 1 == len(won_ids) and i not in won_ids):
                        card[card==-1]=0
                        sum = np.sum(card)
                        print('WIN ',sum * d)
                    else:
                        won = True
                        won_ids.add(i)
            if(won):
                continue            
                    
            for col in range(card.shape[1]):
                isWinning = True
                for y in card[:,col]:
                    if y != -1:
                        isWinning = False
                if(isWinning):
                    if(len(cards) - 1 == len(won_ids) and i not in won_ids):
                        card[card==-1]=0
                        sum = np.sum(card)
                        print('WIN ',sum * d)
                    else:
                        won_ids.add(i) 

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