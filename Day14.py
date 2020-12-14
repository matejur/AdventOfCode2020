def getAddresses(addr, mask):
    addr = bin(addr)[2:].zfill(36)
    result = []
    numsOfX = 0

    for i,b in enumerate(mask):
        if b == "0":
            result.append(addr[i])
        elif b == "1":
            result.append("1")
        elif b == "X":
            numsOfX += 1
            result.append("X")

    possibilities = 2 ** numsOfX
    out = []

    for i in range(possibilities):
        posibility = bin(i)[2:].zfill(numsOfX)
        maskIndex = 0
        newAddr = []

        for j in result:
            if j == "X":
                newAddr.append(posibility[maskIndex])
                maskIndex += 1
            else:
                newAddr.append(j)
        
        out.append(int("".join(newAddr),2))

    return out
        
    

def applyMask(number, mask):
    number = bin(number)[2:].zfill(36)
    out = []

    for i,b in enumerate(mask):
        if b == "X":
            out.append(number[i])
        else:
            out.append(b)

    return int("".join(out), 2)

with open("input14.txt", "r") as f:
    program = f.readlines()

    mask = None
    memory1 = {}
    memory2 = {}
    
    for line in program:
        line = line.split(" = ")

        if line[0] == "mask":
            mask = line[1]
        else:
            pos = int(line[0][4:len(line[0]) - 1])

            memory1[pos] = applyMask(int(line[1]), mask)

            addrs = getAddresses(pos, mask)

            for addr in addrs:
                memory2[addr] = int(line[1])

    print(f"PART 1: {sum(memory1.values())}")
    print(f"PART 2: {sum(memory2.values())}")
