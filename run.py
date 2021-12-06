import argparse
import os
import importlib
import logging

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

    mylogger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    mylogger.addHandler(handler)

    directories = [x for x in os.listdir() if is_int(x)]

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
            with open(f"{day}/test.txt") as testdata:
                result = runner.main(testdata)
        else:
            print("Running Advent of Code 2021 day",day,"with live data")
            with open(f"{day}/input.txt") as inputdata:
                result = runner.main(inputdata)

        print("Part A:", result[0])
        print("Part B:", result[1])