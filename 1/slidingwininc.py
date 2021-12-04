with open("sonar.txt") as sonar:
    # create a list of the last 3 values and their sum
    previouslist = list((0,0,0))
    for init in range(3):
        depthstr = sonar.readline()
        previouslist[init] = int(depthstr.strip())
    previoussum = sum(previouslist)
    increases = 0

    for depthstr in sonar.readlines():
        depth = int(depthstr.strip())
        debugstr = f"{previouslist}={previoussum}"
        previouslist = previouslist[1:] + [depth]
        currentsum = sum(previouslist)
        debugstr += f" {previouslist}={currentsum}"
        if currentsum > previoussum:
            increases += 1
            debugstr += " increased"
        previoussum = currentsum
        print(debugstr)
print(increases)