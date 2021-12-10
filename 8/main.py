import io
import itertools
import os

def is_1478 (segments: str, include8 = True) -> bool:
    "returns true if the segments are a 1, 4, 7 or 8"
    numsegs = len(segments)
    if numsegs == 2 or numsegs == 4 or numsegs == 3: # 1, 4 or 7
        return True
    elif include8 and numsegs == 7: # 8
        return True
    return False

def possibles (isegments: list, osegments: list) -> int:
    output_string = ''

    num_found = [ False for nf in range(10) ]
    for seg in itertools.chain(isegments, osegments):
        numsegs = len(seg)
        if numsegs == 2: # 1
            num_found[1] = True
            one = set(seg)
        elif numsegs == 4: # 4
            num_found[4] = True
            four = set(seg)
        elif numsegs == 3: # 7
            num_found[7] = True
            seven = set(seg)

    if num_found[4] and (num_found[1] or num_found[7]):
        if not num_found[1]: # need to work out a one
            one = four.intersection(seven)
        four_diff_one = four.difference(one)

        for seg in osegments:
            numsegs = len(seg)
            if numsegs == 2: # 1
                output_string += '1'
            elif numsegs == 3: # 7
                output_string += '7'
            elif numsegs == 4: # 4
                output_string += '4'
            elif numsegs == 5: # 2, 3 or 5
                segset = set(seg)
                if one.issubset(segset): # 3
                    output_string += '3'
                elif four_diff_one.issubset(segset): # 5
                    output_string += '5'
                else: # 2
                    output_string += '2'
            elif numsegs == 6: # 0, 6 ot 9
                segset = set(seg)
                if not one.issubset(segset): # 6
                    output_string += '6'
                elif not four_diff_one.issubset(segset): # 0
                    output_string += '0'
                else: # 9
                    output_string += '9'
            elif numsegs == 7: # 8
                output_string += '8'
            else:
                print("This is not a segment display")
    else:
        print(num_found, "Not enough info to decode line")

    return int(output_string)

def main (stream: io.IOBase) -> tuple:
    partA = partB = 0
    for signals in stream.readlines():
        inputsignals, outputsignals, *otherinput = signals.split('|')
        inputs = [i.strip() for i in inputsignals.strip().split()]
        outputs = [o.strip() for o in outputsignals.strip().split()]
        partA += sum(1 for o in outputs if is_1478(o))
        partB += possibles(inputs,outputs)
    return (partA,partB)