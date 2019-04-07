steps = int(input())

def ways(steps):
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps == 3:
        return 4
    return ways(steps-1)+ways(steps-2)+ways(steps-3)

print("%d steps has %d ways to climb" % (steps, ways(steps)))