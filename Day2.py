with open("input2.txt", "r") as f:
    lines = f.readlines()
    validPasswords1 = 0
    validPasswords2 = 0

    for line in lines:
        policy = line.split(":")[0]
        password = line.split(": ")[1]

        letter = policy.split(" ")[1]
        minMax = policy.split(" ")[0]
        minimum = int(minMax.split("-")[0])
        maximum = int(minMax.split("-")[1])

        counter = 0

        for l in password:
            if l == letter:
                counter += 1

        if (minimum <= counter and counter <= maximum):
            validPasswords1 += 1

        if ((password[minimum - 1] == letter) != (password[maximum - 1] == letter)):
            validPasswords2 += 1
    

    print("Part 1: " + str(validPasswords1))
    print("Part 2: " + str(validPasswords2))
