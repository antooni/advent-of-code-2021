from pathlib import Path

def main():
    path = Path(__file__).resolve().parents[0].joinpath('input.txt')
# PART 1
    counter = 0
    previous = int(open(path).readline())

    with open(path) as f:
        for line in f:
            if previous < int(line):
                counter += 1
            previous = int(line)
            
    print('Part 1 solution: ',counter)

# PART 2
    counter = 0
    lines = []

    with open(path) as f:
        line = f.readline()
        while line:
            lines.append(int(line))
            line = f.readline()

    n = len(lines)

    for i, line in enumerate(lines):
        if (i+3) >= n:
            break

        a = lines[i] + lines[i+1] + lines[i+2]
        b = lines[i+1] + lines[i+2] + lines[i+3]

        if a < b:
            counter += 1

    print('Part 2 solution: ',counter)

if __name__ == "__main__":
    main()

   




