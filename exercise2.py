item = input("What item would you like to buy?: ")
price = float(input(f"How much is the {item}?: "))
quantity = int(input(f"How many {item} would you like to buy?: "))

print(f"{quantity} {item}/s would be ${price*quantity}")