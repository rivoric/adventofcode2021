import io
from itertools import repeat

def left_right (values: str, splitter: str) -> tuple:
    "returns values left and right of the split value as a tuple"
    vleft, vright, *otherinput = values.split(splitter)
    return (vleft.strip(), vright.strip())

def overlap (num):
   return num > 1

class vents ():
    def __init__(self) -> None:
        self._vents = list()

    def _min_max (self) -> tuple:
        if not self._vents: # no data loaded
            return (0,0,0,0)
        minventx = min(self._vents, key = lambda v: min(v[0],v[2])) # returns the smallest
        minx = min(minventx[0],minventx[2])
        minventy = min(self._vents, key = lambda v: min(v[1],v[3]))
        miny = min(minventy[1],minventy[3])
        maxventx = max(self._vents, key = lambda v: max(v[0],v[2]))
        maxx = max(maxventx[0],maxventx[2])
        maxventy = max(self._vents, key = lambda v: max(v[1],v[3]))
        maxy = max(maxventy[1],maxventy[3])
        return (minx,miny,maxx,maxy)

    def load_data (self, vent_data: io.IOBase) -> None:
        for ventstr in vent_data.readlines():
            ventstart, ventend = left_right(ventstr,'->')
            startx, starty = left_right(ventstart,',')
            endx, endy = left_right(ventend,',')
            self._vents.append((int(startx), int(starty), int(endx), int(endy)))

    def number_intersections (self, all_lines = False) -> int:
        minx,miny,maxx,maxy = self._min_max()
        row = [0 for x in repeat(None,maxx+1)] # if my max was 9, create a row of 10 zeros so I can reference the row[9] to make referencing simple
        grid = [row.copy() for y in repeat(None,maxy+1)] # duplicate for all y

        for vent in self._vents:
            if vent[0] == vent[2]: # horizontal line
                x = vent[0]
                if vent[1] < vent[3]: # increaing line
                    for y in range(vent[1],vent[3]+1):
                        grid[y][x] += 1
                else: # decreasing line
                    for y in range(vent[3],vent[1]+1):
                        grid[y][x] += 1
            elif vent[1] == vent[3]: # vertical line
                y = vent[1]
                if vent[0] < vent[2]:
                    for x in range(vent[0],vent[2]+1):
                        grid[y][x] += 1
                else:
                    for x in range(vent[2],vent[0]+1):
                        grid[y][x] += 1
            elif all_lines: # include all lines - this must be a diagonal
                if abs(vent[0] - vent[2]) == abs(vent[1] - vent[3]):
                    #print(vent)
                    if vent[0] < vent[2] and vent[1] < vent[3]: # x and y increasing
                        #debug = ""
                        for step in range(vent[2]-vent[0]+1):
                            #debug += f"{vent[1]+step},{vent[0]+step} "
                            grid[vent[1]+step][vent[0]+step] += 1
                        #print(debug)
                    if vent[0] < vent[2] and vent[1] > vent[3]: # x increasing, y decreasing
                        #debug = ""
                        for step in range(vent[2]-vent[0]+1):
                            #debug += f"{vent[1]-step},{vent[0]+step} "
                            grid[vent[1]-step][vent[0]+step] += 1
                        #print(debug)
                    if vent[0] > vent[2] and vent[1] < vent[3]: # x decreasing and y increasing
                        #debug = ""
                        for step in range(vent[0]-vent[2]+1):
                            #debug += f"{vent[1]+step},{vent[0]-step} "
                            grid[vent[1]+step][vent[0]-step] += 1
                        #print(debug)
                    if vent[0] > vent[2] and vent[1] > vent[3]: # x and y decreasing
                        #debug = ""
                        for step in range(vent[0]-vent[2]+1):
                            #debug += f"{vent[1]-step},{vent[0]-step} "
                            grid[vent[1]-step][vent[0]-step] += 1
                        #print(debug)
                else:
                    print("Line",vent,"is not diagonal")

        overlaps = 0
        for row in grid:
            overlaps += sum(overlap(v) for v in row)
        return overlaps

def main (stream: io.IOBase) -> tuple:
    all_vents = vents()
    all_vents.load_data(stream)
    partA = all_vents.number_intersections()
    partB = all_vents.number_intersections(all_lines=True)
    return (partA, partB)
