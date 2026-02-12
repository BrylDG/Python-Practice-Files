a = "ABCABCABCB"

def sortCounter(a):
    letters = set(a)
    sortedA = sorted(list(a))
    map = {}

    for i in letters:
        map[i] = sortedA.count(i)

    temp_list = []
    for j in map:
        temp_list.append(f"{map[j]}{j}")

    output = "".join(temp_list)

    print(output)

sortCounter(a)
