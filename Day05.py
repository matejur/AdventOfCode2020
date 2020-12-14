def getID(code):
    row = 0
    column = 0
    
    for i in range(7):
        row *= 2
        if code[i] == "B": # binary 1
            row += 1
        elif code[i] == "F": # binary 0
            row += 0

    for i in range(7,10):
        column *= 2
        if code[i] == "R": # binary 1
            column += 1
        elif code[i] == "L": # binary 0
            column += 0

    return row * 8 + column



with open("input5.txt", "r") as f:
    seats = [getID(line) for line in f.readlines()]
    
    print("PART 1: " + str(max(seats)))
    
    seats.sort()

    for i in range(len(seats) - 1):
        if (seats[i] + 2 == seats[i+1]):
            print("PART 2: " + str(seats[i] + 1))
            break

    
    
