def getNeighbours(cube, dim):
    x,y,z,w = cube
    neighbours = set()
    for diffX in range(-1,2):
        for diffY in range(-1,2):
            for diffZ in range(-1,2):

                if not dim:
                    if diffX is 0 and diffY is 0 and diffZ is 0:
                        continue
                    newCube = (x+diffX, y+diffY, z+diffZ, w)
                    neighbours.add(newCube)
                else:
                    for diffW in range(-1,2):
                        if diffX is 0 and diffY is 0 and diffZ is 0 and diffW is 0:
                            continue
                        newCube = (x+diffX, y+diffY, z+diffZ, w+diffW)
                        neighbours.add(newCube)

    return neighbours

def simulate(activeCubes, dim):
    for _ in range(6):
        newActiveCubes = set()
        
        for cube in activeCubes:
            neighbours = getNeighbours(cube, dim == 4)

            if len([x for x in neighbours if x in activeCubes]) in [2,3]:
                newActiveCubes.add(cube)

            for neighbour in neighbours:
                neighbours2 = getNeighbours(neighbour, dim == 4)
                if len([x for x in neighbours2 if x in activeCubes]) is 3:
                    newActiveCubes.add(neighbour)

        activeCubes = newActiveCubes

    return len(activeCubes)
                    

with open("input17.txt", "r") as f:
    activeCubes = set()

    for x,line in enumerate(f.readlines()):
        for y,cube in enumerate(line):
            if cube == "#":
                activeCubes.add((x,y,0,0))

    print(f"PART 1: {simulate(activeCubes,3)}")
    print(f"PART 2: {simulate(activeCubes,4)}")
