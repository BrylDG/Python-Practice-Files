inputArray = list(map(int, input().split(",")))
closest = inputArray[0]

for x in inputArray:
    if abs(x) < abs(closest):
        closest = x
    elif abs(x) == abs(closest) and x > closest:
        closest = x

print(closest)

