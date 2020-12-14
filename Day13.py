with open("input13.txt", "r") as f:
    earliest = int(f.readline())
    buses = [int(x) if x is not "x" else None for x in f.readline().split(",")]

    bestBus = 0
    bestTime = 0

    for bus in buses:
        if bus is None:
            continue
        first = int(earliest / bus)

        time = first * bus

        while time < earliest:
            time += bus

        wait = time - earliest
        
        if bestTime > wait or bestTime == 0:
            bestBus = bus
            bestTime = wait


    print(f"PART 1: {bestBus * bestTime}")

    time = 0
    diff = 1
    for delta, bus in enumerate(buses):
        if bus is None: continue
        while True:
            if(delta + time) % bus == 0: break
            time += diff   
        diff *= bus

    print(f"PART 2: {time}")
            

    
