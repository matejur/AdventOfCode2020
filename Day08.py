def getOperationAndArgument(command):
    command = command.split(" ")
    operation = command[0]
    argument = int(command[1])

    return operation, argument

def evaluate(commands, first):

    index = 0
    accumulator = 0

    while index < len(commands):
        if commands[index][1]:
            if first:
                return accumulator
            return -1
        
        operation, argument = getOperationAndArgument(commands[index][0])
        commands[index][1] = True

        if operation == "acc":
            accumulator += argument

        elif operation == "jmp":
            index += argument
            continue

        index += 1

    return accumulator
    

with open("input8.txt", "r") as f:
    commands = [[command.rstrip(), False] for command in f.readlines()]

    print(f"PART 1: {evaluate(commands, True)}")

    for command in commands:
        operation, argument = getOperationAndArgument(command[0])

        if operation == "jmp":
            command[0] = "nop " + str(argument)
        elif operation == "nop":
            command[0] = "jmp " + str(argument)
        elif operation == "acc":
            continue

        acc = evaluate(commands, False)

        command[0] = f"{operation} {argument}"
        
        for command in commands:
            command[1] = False
            
        if acc != -1:
            print(f"PART 2: {acc}")
            break

        

    
        
