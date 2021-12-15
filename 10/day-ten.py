from pathlib import Path

path = Path(__file__).resolve().parent.joinpath('input.txt')

lines = open(path).readlines()

OPENING_BRACKETS = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

INVALID_SCORING = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

invalid_score = 0
dangling_brackets = []

for line in lines:
    line = line.strip('\n')
    syntax_stack = []
    
    for c in line:
        if c in ['[','(','{','<']:
            syntax_stack.append(c)
            
        elif c in [']',')','}','>']:
            if OPENING_BRACKETS[c] != syntax_stack[len(syntax_stack)-1]:
                invalid_score += INVALID_SCORING[c]
                syntax_stack = []
                break
            else:
                syntax_stack.pop(len(syntax_stack)-1)

    if len(syntax_stack):
        dangling_brackets.append(syntax_stack)
        
print('PART 1 - invalid score: ', invalid_score)
        
AUTOCOMPLETE_SCORING = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

autocomplete_scores = []
for line in dangling_brackets:
    tmp = 0
    line.reverse()
    for c in line:
        tmp = tmp*5 + AUTOCOMPLETE_SCORING[c]
    autocomplete_scores.append(tmp)
    
print('PART 2 - autocomplete score: ',sorted(autocomplete_scores)[int(len(autocomplete_scores)/2)])