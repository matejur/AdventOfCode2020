masterBags = {}
mustContain = {}
queue = []
validBags = set()

def part2(bagName):    
    if (bagName not in mustContain):
        return 1

    bags = 0
    for bag in mustContain[bagName]:
        bags += bag[0] * part2(bag[1])

    return 1 + bags

with open("input7.txt", "r") as f:
    rules = f.readlines()

    for rule in rules:
        rule = rule.rstrip().split(" contain ")
        masterBag = rule[0].replace(" bags", "")
        contents = rule[1].replace(".", "").split(", ")

        for bag in contents:
            data = bag.split()
            bag = f"{data[1]} {data[2]}"

            if bag == "other bags":
                continue

            number = int(data[0])

            if masterBag in mustContain:
                mustContain[masterBag].append([number, bag])
            else:
                mustContain[masterBag] = [[number, bag]]

            if bag in masterBags:
                masterBags[bag].add(masterBag)
            else:
                masterBags[bag] = {masterBag}

    for bag in masterBags["shiny gold"]:
        queue.append(bag)

    while(len(queue) != 0):
        curr = queue.pop(0)
        validBags.add(curr)

        if curr in masterBags:
            for bag in masterBags[curr]:
                queue.append(bag)
        
    print(f"PART 1: {len(validBags)}")
    print(f"PART 2: {part2('shiny gold') - 1}")


