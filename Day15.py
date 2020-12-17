def simulate(numbers, turns):
    alreadySpoken = {}
    prev = 0

    for turn, number in enumerate(numbers):
        alreadySpoken[int(number)] = [turn + 1]
        prev = int(number)

    for turn in range(len(numbers) + 1, turns + 1):
        if len(alreadySpoken[prev]) > 1:
            newNumber = alreadySpoken[prev][1] - alreadySpoken[prev][0]
            alreadySpoken[prev].pop(0)
        else:
            newNumber = 0

        if newNumber in alreadySpoken:
            alreadySpoken[newNumber].append(turn)
        else:
            alreadySpoken[newNumber] = [turn]
        
        prev = newNumber

    return prev
    

numbers = input("Puzzle input: ").split(",")


    
print(f"PART 1: {simulate(numbers, 2020)}")
print(f"PART 2: {simulate(numbers, 30000000)}")
        

    
