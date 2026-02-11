days = [7, 1, 5, 3, 6, 4]
max_profit = 0
min_price = float('inf')

for i in range(len(days)):
    if i < min_price:
        min_price = i
    elif (i - min_price) > max_profit:
        max_profit = i - min_price

print(max_profit)