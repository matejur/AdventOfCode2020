import re

with open("input4.txt", "r") as f:
    current = {}
    passports = []
    counter1 = 0
    counter2 = 0

    for line in f.readlines():
        if line != "\n":
            data = line.split(" ")

            for field in data:
                fields = field.split(":")
                current[fields[0]] = fields[1].rstrip()

        else:
            passports.append(current)   
            current = {}

    passports.append(current)

    for passport in passports:
        if ("byr" in passport and "iyr" in passport and "eyr" in passport and
            "hgt" in passport and "hcl" in passport and "ecl" in passport and
            "pid" in passport):
                counter1 += 1

                byr = 1920 <= int(passport["byr"]) and int(passport["byr"]) <= 2002
                iyr = 2010 <= int(passport["iyr"]) and int(passport["iyr"]) <= 2020
                eyr = 2020 <= int(passport["eyr"]) and int(passport["eyr"]) <= 2030
                
                hgt = False
                if("cm" in passport["hgt"]):
                    n = passport["hgt"]
                    height = int(n[:len(n)-2])
                    hgt = 150 <= height and height <= 193
                    
                elif("in" in passport["hgt"]):
                    n = passport["hgt"]
                    height = int(n[:len(n)-2])
                    hgt = 59 <= height and height <= 76

                hcl = re.search("#[a-f0-9]{6}", passport["hcl"]) is not None

                ecl = passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                
                pid = re.search("^\d{9}$", passport["pid"]) is not None

                if (byr and iyr and eyr and hgt and hcl and ecl and pid):
                    counter2 += 1

                

                

    print("PART 1: " + str(counter1))
    print("PART 2: " + str(counter2))
