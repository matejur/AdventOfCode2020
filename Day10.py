with open("input10.txt", "r") as f:
    adapters = sorted([int(x) for x in f.readlines()])
    
    diff1 = 0
    diff3 = 1 # device always has a difference of 3
    differences = [0 for x in range(len(adapters))]

    prev = 0
    for i, adapter in enumerate(adapters):
        diff = adapter - prev
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 += 1

        differences[i] = diff
        
        prev = adapter

    
    numberOfOnes = 0
    gaps = {}

    for diff in differences:
        if diff == 1:
            numberOfOnes += 1
        elif diff == 3:
            if numberOfOnes in gaps:
                gaps[numberOfOnes] += 1
            else:
                gaps[numberOfOnes] = 1
            numberOfOnes = 0

    gaps[numberOfOnes] += 1

    part2 = 1

    for key, value in gaps.items():
        if key == 4: n = 7
        elif key == 3: n = 4
        elif key == 2: n = 2
        else: n = 1
        part2 *= n ** value
        
    print(f"PART 1: {diff1 * diff3}")
    print(f"PART 2: {part2}")

    
