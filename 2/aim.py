with open("directions.txt") as directions:
    horizontal = depth = aim = 0
    for directionstr in directions.readlines():
        # first attempt, works for all versions of Python
        # direction, distancestr, *otherinput = directionstr.split()
        # distance = int(distancestr)
        # if direction == 'forward':
        #     horizontal += distance
        #     depth += (aim * distance)
        # elif direction == 'down':
        #     aim += distance
        # elif direction == 'up':
        #     aim -= distance
        # else:
        #     print("Invalid direction:",direction,"of",distance)

        # Requires Python 3.10
        match directionstr.split():
            case ['forward', distance]:
                dist = int(distance)
                horizontal += dist
                depth += (aim * dist)
            case ['down', distance]:
                aim += int(distance)
            case ['up', distance]:
                aim -= int(distance)
            case [direction, distance]:
                print("Invalid direction:",direction,"of",distance)

print("Horizontal distance:",horizontal,"\nDepth:",depth,"\nSum:",horizontal*depth)
