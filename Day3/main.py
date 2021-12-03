from copy import deepcopy

def part1(input):
    mostCommonBinary = leastCommonBinary = ''
    for index in range(len(lines[0])):
        ones = zeros = 0
        for binary in lines:
            match binary[index]:
                case '0':
                    zeros += 1
                case '1':
                    ones += 1
        if ones >= zeros:
            mostCommonBinary += '1'
            leastCommonBinary += '0'
        else:
            mostCommonBinary += '0'
            leastCommonBinary += '1'
    return int(mostCommonBinary, 2) * int(leastCommonBinary, 2)

def part2(inputList, type):
    for index in range(len(inputList[0])):
        if len(inputList) == 1:
            return inputList[0]
        zeros = ones = 0
        for binary in inputList:
            if binary[index] == '0':
                zeros += 1
            elif binary[index] == '1':
                ones += 1
        if type == 'mostCommon':
            if ones >= zeros:
                listFilter = filter(lambda word: word[index] == '1', inputList)
                inputList = list(listFilter)
            else :
                listFilter = filter(lambda word: word[index] == '0', inputList)
                inputList = list(listFilter)
        elif type == 'leastCommon':
            if ones >= zeros:
                listFilter = filter(lambda word: word[index] == '0', inputList)
                inputList = list(listFilter)
            else :
                listFilter = filter(lambda word: word[index] == '1', inputList)
                inputList = list(listFilter)
    return inputList[0]

with open('input.txt') as file:
    lines = [line.rstrip() for line in file.readlines()]
    print(f'Power consumption: {part1(lines)}')
    lifeSupportRating = int(part2(lines, 'mostCommon'), 2) * int(part2(lines, 'leastCommon'), 2)
    print(f'Life support rating: {lifeSupportRating}')

        
