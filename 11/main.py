import io

class bdo (): # bioluminescent dumbo octopuses
    def __init__(self, cavern) -> None:
        self._octopodes = list()
        self._flashed = list()
        self._maxx = 0
        self._maxy = 0
        self._day = 0
        for octo in cavern.readlines():
            octoline = octo.strip()
            if len(octoline) > 0: # not a blank line
                # one matrix for octopodes
                line = [ int(x) for x in octoline ]
                self._maxy += 1
                self._octopodes.append(line)
                if self._maxx == 0:
                    self._maxx = len(line)
                else:
                    if self._maxx != len(line):
                        print("Different line lengths")
                # one matrix to keep track of them flashing
                line = [ False for x in range(self._maxx) ]
                self._flashed.append(line)

    def _inc (self, x: int, y: int) -> int:
        self._octopodes[y][x] += 1
        return self._octopodes[y][x]

    def _reset (self, x: int, y: int) -> int:
        old = self._octopodes[y][x]
        self._octopodes[y][x] = 0
        return old

    def show_cavern (self) -> None:
        print("Cavern, day",self._day)
        for line in self._octopodes:
            print(line)

    def next_day (self) -> int:
        flashed = 0
        self._day += 1

        # ensure flashed matrix is false
        for y in range(self._maxy):
            for x in range(self._maxx):
                self._flashed[y][x] = False
                self._inc(x,y)

        repeat_loop = True
        while repeat_loop:
            repeat_loop = False
            for y in range(self._maxy):
                for x in range(self._maxx):
                    if self._octopodes[y][x] > 9 and not self._flashed[y][x]:
                        self._flashed[y][x] = True
                        flashed += 1
                        repeat_loop = True

                        if x > 0 and y > 0:
                            self._inc(x-1,y-1)
                        if x > 0:
                            self._inc(x-1,y)
                        if x > 0 and y < self._maxy - 1:
                            self._inc(x-1,y+1)
                        if y > 0:
                            self._inc(x,y-1)
                        if y < self._maxy - 1:
                            self._inc(x,y+1)
                        if x < self._maxx - 1 and y > 0:
                            self._inc(x+1,y-1)
                        if x < self._maxx - 1:
                            self._inc(x+1,y)
                        if x < self._maxx - 1 and y < self._maxy - 1:
                            self._inc(x+1,y+1)


        for y in range(self._maxy):
            for x in range(self._maxx):
                if self._flashed[y][x]:
                    self._reset(x,y)

        return flashed

def main (stream: io.IOBase) -> tuple:
    partA = partB = 0
    octopi = bdo(stream)

    for day in range(100):
        flashes = octopi.next_day() 
        partA += flashes

        if flashes == 100 and partB == 0:
            partB = day + 1 # starting a day 0 not day 1

    if partB == 0: # still not found the first day
        flashes = 0
        while flashes < 100:
            day += 1
            flashes = octopi.next_day()
        partB = day + 1 # starting a day 0 not day 1

    return (partA,partB)