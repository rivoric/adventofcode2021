import io

def msb (zeros: int, ones: int):
    if zeros > ones:
        return '0'
    if zeros < ones:
        return '1'
    else:
        return '='

def lsb (zeros: int, ones: int):
    if zeros < ones:
        return '0'
    if zeros > ones:
        return '1'
    else:
        return '='

class bitiness ():
    def __init__(self, diag) -> None:
        self._numdiagbits = len(diag)
        self._bits = [ list((0,0)) for x in range(self._numdiagbits) ]
        self.mapper(diag)

    def mapper(self, diag) -> None:
        for bitnum in range(min(self._numdiagbits,len(diag))):
            bit = diag[bitnum]
            if bit >= '0' and bit <= '1': # ensure in range
                self._bits[bitnum][int(bit)] += 1
            else:
                print("Invalid diagnostic bit",bit)

    def numofbits(self) -> int:
        return self._numdiagbits

    def msb(self, position: int) -> str:
        return msb(self._bits[position][0],self._bits[position][1])

    def lsb(self, position: int) -> str:
        return lsb(self._bits[position][0],self._bits[position][1])

    def gamma(self) -> str:
        return ''.join([msb(x[0],x[1]) for x in self._bits])

    def epsilon(self) -> str:
        return ''.join([lsb(x[0],x[1]) for x in self._bits])

def diagnostic (stream: io.IOBase) -> None:
    diaglist = [ x.strip() for x in stream.readlines()]
    diag = bitiness(diaglist[0])
    for line in range(1,len(diaglist)):
        diag.mapper(diaglist[line])

    # gamma = diag.gamma()
    # epsilon = diag.epsilon()
    # print("Gamma:", gamma, int(gamma,2))
    # print("epsilon", epsilon, int(epsilon,2))
    # print("Sum", int(gamma,2) * int(epsilon,2))

    ogrlist = diaglist.copy()
    for pos in range(diag.numofbits()):
        ogrdiag = bitiness(ogrlist[0])
        for line in range(1,len(ogrlist)):
            ogrdiag.mapper(ogrlist[line])
        msb = ogrdiag.msb(pos)
        if msb == '=':
            msb = '1' # If 0 and 1 are equally common, keep values with a 1 in the position being considered
        ogrlist = [ x for x in ogrlist if x[pos] == msb]
        if len(ogrlist) <= 1:
            break
    print("oxygen generator rating:", ogrlist[0], int(ogrlist[0],2))

    co2srlist = diaglist.copy()
    for pos in range(diag.numofbits()):
        co2srdiag = bitiness(co2srlist[0])
        for line in range(1,len(co2srlist)):
            co2srdiag.mapper(co2srlist[line])
        lsb = co2srdiag.lsb(pos)
        if lsb == '=':
            lsb = '0' # If 0 and 1 are equally common, keep values with a 0 in the position being considered
        co2srlist = [ x for x in co2srlist if x[pos] == lsb]
        if len(co2srlist) <= 1:
            break
    print("CO2 scrubber rating:", co2srlist[0], int(co2srlist[0],2))
    print("life support rating:", int(ogrlist[0],2) * int(co2srlist[0],2))

if __name__ == "__main__":
    testdata = io.StringIO("""00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""")
    print("Test data")
    diagnostic(testdata)

    print("Live data")
    with open("input.txt") as diagnostics:
        diagnostic(diagnostics)