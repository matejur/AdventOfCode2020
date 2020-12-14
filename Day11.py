from copy import deepcopy
import time

def countAllOccupied(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == "#":
                count += 1

    return count
    
def countNeighbours(x,y,seats):
    adjacent = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i != 0 or j != 0:
                newX = x + i
                newY = y + j
                if newY > -1 and newY < len(seats) and newX > -1 and newX < len(seats[newY]):
                    if seats[newY][newX] == "#":
                        adjacent += 1

    return adjacent

def countFarNeighbours(x,y,seats):
    newX = x
    newY = y
    count = 0
    
    #levo
    while newX > 0:
        newX -= 1
        if seats[y][newX] == "#":
            count += 1
            break
        elif seats[y][newX] == "L":
            break
    #desno
    newX = x

    while newX < len(seats[y]) - 1:
        newX += 1
        if seats[y][newX] == "#":
            count += 1
            break
        elif seats[y][newX] == "L":
            break

    #gor
    while newY > 0:
        newY -= 1
        if seats[newY][x] == "#":
            count += 1
            break
        elif seats[newY][x] == "L":
            break

    #dol
    newY = y
    while newY < len(seats) - 1:
        newY += 1
        if seats[newY][x] == "#":
            count += 1
            break
        elif seats[newY][x] == "L":
            break

    #gor levo
    newY = y
    newX = x
    while newY > 0 and newX > 0:
        newY -= 1
        newX -= 1

        if seats[newY][newX] == "#":
            count += 1
            break
        elif seats[newY][newX] == "L":
            break

    #gor desno
    newY = y
    newX = x
    while newY > 0 and newX < len(seats[y]) - 1:
        newY -= 1
        newX += 1

        if seats[newY][newX] == "#":
            count += 1
            break
        elif seats[newY][newX] == "L":
            break

    #dol desno
    newY = y
    newX = x
    while newY < len(seats) - 1 and newX < len(seats[y]) - 1:
        newY += 1
        newX += 1

        if seats[newY][newX] == "#":
            count += 1
            break
        elif seats[newY][newX] == "L":
            break

    #dol levo
    newY = y
    newX = x
    while newY < len(seats) - 1 and newX > 0:
        newY += 1
        newX -= 1

        if seats[newY][newX] == "#":
            count += 1
            break
        elif seats[newY][newX] == "L":
            break
        

    return count
        
                

def simulate(x,y,seats,nextIteration):
    state = seats[y][x]

    if state == "L":
        adjacent = countNeighbours(x,y,seats)
        if adjacent == 0:
            nextIteration[y][x] = "#"
        else:
            nextIteration[y][x] = "L"

    elif state == "#":
        adjacent = countNeighbours(x,y,seats)
        if adjacent >= 4:
            nextIteration[y][x] = "L"
        else:
            nextIteration[y][x] = "#"
    else:
        nextIteration[y][x] = "."

def simulate2(x,y,seats,nextIteration):
    state = seats[y][x]

    if state == "L":
        adjacent = countFarNeighbours(x,y,seats)
        if adjacent == 0:
            nextIteration[y][x] = "#"
        else:
            nextIteration[y][x] = "L"

    elif state == "#":
        adjacent = countFarNeighbours(x,y,seats)
        if adjacent >= 5:
            nextIteration[y][x] = "L"
        else:
            nextIteration[y][x] = "#"
    else:
        nextIteration[y][x] = "."

def nicePrint(i):
    for a in i:
        print("".join(a))


with open("input11.txt", "r") as f:
    starting = [list(seat.rstrip()) for seat in f.readlines()]
    seats1 = deepcopy(starting)

    seats2 = [["" for x in range(len(seats1[y]))] for y in range(len(seats1))]

    t1 = time.time()
    while True:
        for y in range(len(seats1)):
            for x in range(len(seats1[y])):
                simulate(x,y,seats1,seats2)
                
        for y in range(len(seats1)):
            for x in range(len(seats1[y])):
                simulate(x,y,seats2,seats1)

        if seats1 == seats2:
            print(f"PART 1: {countAllOccupied(seats1)}   TIME: {round(time.time()-t1, 2)}s")
            break

    seats1 = deepcopy(starting)

    t1 = time.time()
    while True:
        for y in range(len(seats1)):
            for x in range(len(seats1[y])):
                simulate2(x,y,seats1,seats2)
                
        for y in range(len(seats1)):
            for x in range(len(seats1[y])):
                simulate2(x,y,seats2,seats1)

        if seats1 == seats2:
            print(f"PART 2: {countAllOccupied(seats1)}   TIME: {round(time.time()-t1, 2)}s")
            break

            
