def move(northPos, eastPos, direction, value):
    if action == "N":
        northPos += value
    elif action == "S":
        northPos -= value
    elif action == "E":
        eastPos += value
    elif action == "W":
        eastPos -= value

    return northPos, eastPos

with open("input12.txt", "r") as f:
    instructions = [[row[0], int(row[1:])] for row in f.readlines()]

    # east: 0 south: 1 west: 2 north: 3
    facing = 0
    eastPos = 0
    northPos = 0

    for instr in instructions:
        action = instr[0]
        value = instr[1]
        rotation = value / 90

        if action == "L":
            facing = ((facing - rotation) + 4) % 4
        elif action == "R":
            facing = (facing + rotation) % 4
        elif action == "F":
            if facing == 0:
                eastPos += value
            elif facing == 1:
                northPos -= value
            elif facing == 2:
                eastPos -= value
            elif facing == 3:
                northPos += value
        else:
            northPos, eastPos = move(northPos, eastPos, action, value)

    dist = abs(eastPos) + abs(northPos)
    print(f"PART 1: {dist}")

    waypointEast = 10
    waypointNorth = 1
    shipEast = 0
    shipNorth = 0
    
    for instr in instructions:
        action = instr[0]
        value = instr[1]
        rotation = int(value / 90)

        if action == "L":
            for i in range(rotation):
                tmp = waypointEast
                waypointEast = -waypointNorth
                waypointNorth = tmp
        elif action == "R":
            for i in range(rotation):
                tmp = waypointEast
                waypointEast = waypointNorth
                waypointNorth = -tmp
        elif action == "F":
            for i in range(value):
                shipNorth += waypointNorth
                shipEast += waypointEast
        else:
            waypointNorth, waypointEast = move(waypointNorth, waypointEast, action, value)
            
    dist = abs(shipEast) + abs(shipNorth)
    print(f"PART 2: {dist}")


    
    
