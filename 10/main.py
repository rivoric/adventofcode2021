import io

PAIRS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

ERROR_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

AUTO_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def parse (line: str) -> str:
    openers = list()
    last_opener = ''
    for char in line:
        if char in PAIRS.keys(): # open character, new chunk
            openers.append(last_opener)
            last_opener = char
        elif char in PAIRS.values(): # close character
            if char == PAIRS[last_opener]: # chunk closed
                last_opener = openers.pop()
            else:
                return char,''
        else:
            print("Invalid character")
    
    autocomplete = ''
    while last_opener != '': # need to autocomplete
        autocomplete += PAIRS[last_opener]
        last_opener = openers.pop()

    return '',autocomplete

def main (stream: io.IOBase) -> tuple:
    partA = partB = 0
    autoscores = list()
    for nav_line in stream.readlines():
        nav_subsystem = nav_line.strip()
        error, autocomplete = parse(nav_subsystem)
        if error == '': # incomplete line
            linescore = 0
            for char in autocomplete:
                linescore = linescore * 5 + AUTO_SCORE[char]
            autoscores.append(linescore)
        elif error in ERROR_SCORE.keys(): # corrupt line, score for part A
            partA += ERROR_SCORE[error]
        else:
            print("Invalid error returned")
    autoscores.sort()
    if len(autoscores) % 2 == 1: # odd number of elements, take the middle one
        pos = len(autoscores) // 2 # ensure this is an int
        partB = autoscores[pos]
    else: # even number means there are 2 middle values, take the average
        pos = len(autoscores) // 2
        partB = (autoscores[pos-1] + autoscores[pos]) / 2 
    return (partA,partB)