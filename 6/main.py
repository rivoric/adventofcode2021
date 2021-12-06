import io

class laternfish ():
    def __init__(self) -> None:
        self._laternfishes = list()
        self._numberfishes = list()

    def add_fish (self, days_to_bred = 8) -> None:
        self._laternfishes.append(days_to_bred)
        self._numberfishes.append(1)

    def next_day (self) -> int:
        newfish = 0
        for f in range(len(self._laternfishes)):
            if self._laternfishes[f] == 0:
                self._laternfishes[f] = 6
                newfish += self._numberfishes[f]
            else:
                self._laternfishes[f] -= 1
        if newfish > 0:
            self._laternfishes.append(8)
            self._numberfishes.append(newfish)
        return self.count()

    def count (self) -> int:
        return sum(self._numberfishes)

def main (stream: io.IOBase) -> tuple:
    fishes = laternfish()
    for f in stream.readline().split(','):
        fishes.add_fish(int(f.strip()))
    for d in range(80):
        fishes.next_day()
    parta = fishes.count()
    for d in range(256-80):
        fishes.next_day()
    partb = fishes.count()
    return (parta,partb)