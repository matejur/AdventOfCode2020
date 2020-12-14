with open("input1.txt", "r") as f:
    lines = f.readlines()
    numbers = []

    for line in lines:
        current = int(line)
        
        for number in numbers:
            if (number + current == 2020):
                print("PART 1: " + str(number * current))

            for number2 in numbers:
                if(current + number + number2 == 2020):
                    print("PART 2: " + str(number * number2 * current))
                

        numbers.append(current)
        

