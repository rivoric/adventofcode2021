with open("sonar.txt") as sonar:
    depthstr  = sonar.readline()
    previous  = int(depthstr.strip())
    increases = 0
    for depthstr in sonar.readlines():
        depth = int(depthstr.strip())
        if depth > previous:
            increases += 1
        previous = depth
print(increases)