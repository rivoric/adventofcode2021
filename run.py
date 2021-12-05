import argparse
import os
import io
import importlib

def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Runner for each day')
    parser.add_argument('days', metavar='day', type=int, nargs='*', help='days to run')
    parser.add_argument('-a','--all', action='store_true', help='run for all the days')
    parser.add_argument('-t','--test', action='store_true', help='run with test data')
    args = parser.parse_args()

    directories = [x for x in os.listdir() if is_int(x)]

    testdata = {
        '3': io.StringIO("""00100
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
01010"""),
        '4': io.StringIO("""7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""),
        '5': io.StringIO("""0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2""")
    }

    if args.all:
        days = directories
    else:
        days = list()
        for intday in args.days:
            s = str(intday)
            if s in directories:
                days.append(s)

    for day in days:
        runner = importlib.import_module(f"{day}.main")
        
        if args.test:
            print("Running Advent of Code 2021 day",day,"with test data")
            result = runner.main(testdata[day])
        else:
            print("Running Advent of Code 2021 day",day,"with live data")
            with open(f"{day}/input.txt") as inputdata:
                result = runner.main(inputdata)

        print("Part A:", result[0])
        print("Part B:", result[1])