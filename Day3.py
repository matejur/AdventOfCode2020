slopeRight = 3
slopeDown = 1

gozd = None

with open("input3.txt", "r") as f:
    lines = f.readlines()

    gozd = [0 for x in range(len(lines))]

    for i, line in enumerate(lines):
        gozd[i] = line.rstrip("\n")


def treesHit(slopeR, slopeD):
    startX = 0
    drevesa = 0
    for i, line in enumerate(gozd):
        if (i % slopeD) != 0:
            continue

        while (startX > len(line) - 1):
            line = line + line


        if (line[startX] == "#"):
            drevesa += 1

        startX += slopeR

    return drevesa 


hits = [treesHit(1,1), treesHit(3,1), treesHit(5,1),
        treesHit(7,1), treesHit(1,2)]

part2 = 1
for hit in hits:
    part2 *= hit

print("PART 1:" + str(hits[1]))
print("PART 2:" + str(part2))



