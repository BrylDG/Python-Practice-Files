operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    answer = num1 + num2
elif operator == "-":
    answer = num1 - num2
elif operator == "*":
    answer = num1 * num2
elif operator == "/":
    answer = num1 / num2
else:
    print("Error")

print(answer)