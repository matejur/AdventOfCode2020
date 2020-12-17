import re

with open("input16.txt", "r") as f:
    data = f.read().split("\n\n")

    fields = data[0].split("\n")
    myTicket = data[1].split("\n")[1:]
    otherTickets = data[2].split("\n")[1:]

    acceptedNumbers = set()
    allFields = set()
    validRanges = {}
    
    for field in fields:
        numbers = re.findall(r"\d+", field)
        field = field.split(":")[0]
        allFields.add(field)
        numbers = [int(num) for num in numbers]
        validRanges[field]= numbers
        
        for i in range(numbers[0], numbers[1] + 1):
            acceptedNumbers.add(i)

        for i in range(numbers[2], numbers[3] + 1):
            acceptedNumbers.add(i)

    part1 = 0
    validTickets = []
    
    for ticket in otherTickets:
        values = ticket.split(",")
        valid = True

        for value in values:
            if int(value) not in acceptedNumbers:
                part1 += int(value)
                valid = False
                break
        if valid:
            validTickets.append(ticket)

    allFields = [allFields for x in range(len(myTicket[0].split(",")))]

    for ticket in validTickets:
        values = ticket.split(",")

        for i,value in enumerate(values):
            newFields = set()
            value = int(value)
            for field in allFields[i]:
                boundries = validRanges[field]
                if value >= boundries[0] and value <= boundries[1] or value >= boundries[2] and value <= boundries[3]:
                       newFields.add(field)

            allFields[i] = allFields[i].intersection(newFields)

    allFields = [list(x) for x in allFields]
    alreadyRemoved = set()
    found = False
    while not found:
        toRemove = None
        for fields in allFields:
            if len(fields) == 1 and fields[0] not in alreadyRemoved:
                toRemove = fields[0]
                alreadyRemoved.add(toRemove)
                break

        for fields in allFields:
            if len(fields) != 1 and toRemove in fields:
                fields.remove(toRemove)

        count = 0
        for fields in allFields:
            if len(fields) != 1:
                break
            else:
                count += 1

                if(count == len(allFields)):
                    found = True

    part2 = 1
    for i,number in enumerate(myTicket[0].split(",")):
        if "departure" in allFields[i][0]:
            part2 *= int(number)
            
    print(f"PART 1: {part1}")
    print(f"PART 2: {part2}")
    
