jewels = "aA"
stones = "aAAbbbb"
counter = 0

def countJewels(jewels, stones, counter) -> int:
    for j in set(jewels):
        counter += stones.count(j)

    return counter

print(countJewels(jewels, stones, counter))