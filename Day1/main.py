def problem1(input):
    return sum(y > x for x, y in zip(input, input[1:]))

def problem2(input):
    return sum(x < y for x, y in zip(input, input[3:]))

with open('input.txt') as f:
    lines = [int(line.rstrip()) for line in f]
    print(problem1(lines))
    print(problem2(lines))




