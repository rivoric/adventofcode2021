import io

def low_sum (heightmap: list) -> int:
    "Find the sum (+1) of all the low points"
    sum = 0
    maxx = len(heightmap[0])
    maxy = len(heightmap)
    for y in range(maxy):
        for x in range(maxx):
            low_point = True
            if x > 0 and heightmap[y][x] >= heightmap[y][x-1]:
                low_point = False
            if x < maxx - 1 and heightmap[y][x] >= heightmap[y][x+1]:
                low_point = False
            if y > 0 and heightmap[y][x] >= heightmap[y-1][x]:
                low_point = False
            if y < maxy - 1 and heightmap[y][x] >= heightmap[y+1][x]:
                low_point = False
            if low_point:
                sum += int(heightmap[y][x]) + 1
    return sum

def basin (heightmap: list) -> int:
    "Find all the basins"
    basins = list()
    maxx = len(heightmap[0])
    maxy = len(heightmap)
    for y in range(maxy):
        for x in range(maxx):
            pass
    return 0

def main (stream: io.IOBase) -> tuple:
    heightmap = [ list(h.strip()) for h in stream.readlines() ]
    partA = low_sum(heightmap)
    partB = basin(heightmap)
    return (partA,partB)