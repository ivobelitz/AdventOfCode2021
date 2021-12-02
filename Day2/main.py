def getTuples(file):
    list = []
    for line in file:
        parsedLine = line.rstrip().split()
        tuple = (parsedLine[0], int(parsedLine[1]))
        list.append(tuple)
    return list
 
with open('input.txt') as f:
    tuples = getTuples(f)
    x = 0
    y = 0
    aim = 0
    for movement in tuples:
        direction = movement[0]
        match direction:
            case "forward":
                x += movement[1]
                y += aim * movement[1]
            case "down":
                aim += movement[1]
            case "up":
                aim -= movement[1]
        

