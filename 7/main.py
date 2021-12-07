import io

def constant_cost (all: list, position: int) -> int:
    "calculate the cost as a constant (of 1) for each position"
    cost = 0
    for p in all:
        cost += abs(position - p)
    return cost

def distance_cost (all: list, position: int) -> int:
    "calculate the cost as the sum of the increasing cost per distance"
    cost = 0
    for p in all:
        cost += sum(range(1,abs(position - p)+1))
    return cost

def cost (crabs: list, position: int, cost_method = constant_cost) -> int:
    # work out if moving from this average improves the results
    last_cost = cost_method(crabs,position)

    last_position = position
    new_cost = cost_method(crabs,last_position+1)
    while last_cost > new_cost:
        last_position += 1
        last_cost = new_cost
        #print("Using",last_position,"instead gives",last_cost)
        new_cost = cost_method(crabs,last_position+1)

    last_position = position
    new_cost = cost_method(crabs,last_position-1)
    while last_cost > new_cost:
        last_position -= 1
        last_cost = new_cost
        #print("Using",last_position,"instead gives",last_cost)
        new_cost = cost_method(crabs,last_position-1)

    # last_cost is now the lowest value possible
    return last_cost

def main (stream: io.IOBase) -> tuple:
    crab_position = [int(x.strip()) for x in stream.readline().split(',')]

    # work out the average as a starting point
    avg = round(sum(crab_position)/len(crab_position))

    partA = cost(crab_position,avg)
    partB = cost(crab_position,avg,distance_cost)

    return (partA,partB)