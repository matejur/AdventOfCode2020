with open("input6.txt", "r") as f:
    groups = f.read().split("\n\n")

    count1 = 0
    count2 = 0

    for group in groups:
        group = group.split("\n")

        answers = set()
        answers2 = set()
        first = True;
        
        for person in group:
            if person == "":
                continue
            
            hisAnswers = set()
            
            for answer in person:
                hisAnswers.add(answer)

            answers.update(hisAnswers)
            
            if first:
                answers2.update(hisAnswers)
                first = False
            else:
                answers2 = answers2.intersection(hisAnswers)

        count1 += len(answers)
        count2 += len(answers2)

    print(f"PART 1: {count1}")
    print(f"PART 2: {count2}")
