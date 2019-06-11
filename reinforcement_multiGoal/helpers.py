import math

def getNextPosition(currentPosition, direction):
    x, y = currentPosition
    if direction == "North":
        y += 1
    elif direction == "South":
        y -= 1
    elif direction == "West":
        x -= 1
    elif direction == "East":
        x += 1
    return (x,y)

def optc(node1, node2):
    x1, y1 = node1
    x2, y2 = node2
    return abs(x1-x2) + abs(y1-y2)

def costDif(start, goal, currentPosition, direction):
    nextPosition = getNextPosition(currentPosition, direction)
    costdif = optc(nextPosition, goal) - optc(goal, start)
    return costdif

def isTruthfulStep(start, realGoal, fakeGoals, currentPosition, direction):
    costdif_for_real = costDif(start, realGoal, currentPosition, direction)
    # f = open("testing.txt", "a")
    # f.write("costdif_for_real = " + str(costdif_for_real) + "\n")
    for fakeGoal in fakeGoals:
        costdif_for_fake = costDif(start, fakeGoal, currentPosition, direction)
        # f.write("costdif_for_fake = " + str(costdif_for_fake) + "\n")
        # f.close()
        if costdif_for_real >= costdif_for_fake:
            return False
    return True

def optimality(n_total, n_shortest):
    return (n_total-n_shortest)*1.0/n_shortest

def density(n_truthful):
    if n_truthful:
        return 1.0/n_truthful
    else:
        return float("inf")
