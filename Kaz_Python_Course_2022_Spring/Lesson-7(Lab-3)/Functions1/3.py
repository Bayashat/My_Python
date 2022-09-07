def solve(numheads, numlegs):
    Y = int((numlegs - 2*numheads) / 2)
    X = int(numheads - Y)
    print(f"We have {X} chickens and {Y} rabbits")


l = [int(x) for x in input().split()]
numheads = l[0]
numlegs = l[1]

solve(numheads, numlegs)
