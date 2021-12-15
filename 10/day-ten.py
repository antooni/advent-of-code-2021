from pathlib import Path

path = Path(__file__).resolve().parent.joinpath('input.txt')

lines = open(path).readlines()

corrupted = []

closing_tags = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

incomplete_lines = []

for line in lines:
    line = line.strip('\n')
    syntax_stack = []
    
    incorrect_flag = False
    for c in line:
        if c in ['[','(','{','<']:
            syntax_stack.append(c)
        if c in [']',')','}','>']:
            if closing_tags[c] != syntax_stack[len(syntax_stack)-1]:
                corrupted.append(c)
                incorrect_flag = True
                break
            if closing_tags[c] == syntax_stack[len(syntax_stack)-1]:
                syntax_stack.pop(len(syntax_stack)-1)

    if not incorrect_flag:
        incomplete_lines.append(syntax_stack)


autocomplete_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}



sum = 0 
for c in corrupted:
    sum += scores[c]
print(sum)

auto_results = []
for line in incomplete_lines:
    tmp = 0
    line.reverse()
    for c in line:
        tmp = tmp*5 + autocomplete_scores[c]
    auto_results.append(tmp)

    
    
print(sorted(auto_results)[int(len(auto_results)/2)])