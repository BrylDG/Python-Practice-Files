numbers = [1, 2, 3, 4, 1]

def count(numbers) -> bool:

    for x in numbers:
        if numbers.count(x) > 1:
            return True
            break
        else:
            continue

    return False

print(count(numbers))