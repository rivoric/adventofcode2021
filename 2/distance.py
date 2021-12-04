with open("directions.txt") as directions:
    horizontal = depth = 0
    for directionstr in directions.readlines():
        # first attempt, works in all version of Python
        # direction, distancestr, *otherinput = directionstr.split()
        # distance = int(distancestr)
        # if direction == 'forward':
        #     horizontal += distance
        # elif direction == 'down':
        #     depth += distance
        # elif direction == 'up':
        #     depth -= distance
        # else:
        #     print("Invalid direction:",direction,"of",distance)

        # only works in Python 3.10
        match directionstr.split():
            case ['forward', distance]:
                horizontal += int(distance)
            case ['down', distance]:
                depth += int(distance)
            case ['up', distance]:
                depth -= int(distance)
            case [direction, distance]:
                print("Invalid direction:",direction,"of",distance)

print("Horizontal distance:",horizontal,"\nDepth:",depth,"\nSum:",horizontal*depth)
