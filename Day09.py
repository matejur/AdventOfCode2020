def isSum(number, array):
    if (number == 0): return True
    if (number < 0): return False

    for num in array:
        remainder = number - num
        if (isSum(remainder, array)):
            return True
    
    return False


with open("input9.txt", "r") as f:
    preamble = 25
    inputNumbers = [int(a) for a in f.readlines()]
    part1 = 0

    window = inputNumbers[:preamble]

    for i in range(preamble, len(inputNumbers)):
        current = inputNumbers[i]
        
        if not isSum(current, window.copy()):
            part1 = current
            break

        window.pop(0)
        window.append(current)

    print(f"PART 1: {part1}")

    window = []

    for i in range(len(inputNumbers)):
        current = inputNumbers[i]
        window.append(current)

        while sum(window) > part1:
            window.pop(0)
            
        if sum(window) == part1:
            print(f"PART 2: {min(window) + max(window)}")
            break
        
        
