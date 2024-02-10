# prompts the user for an arithmetic expression
expression = input("Expression: ").split()

x = float(expression[0])
y = expression[1]
z = float(expression[2])

if y == "+":
    print(x + z)

elif y == "-":
    print(x - z)

elif y == "*":
    print(x * z)

elif y == "/":
    result = float(x / z)
    print(round(result, 1))

elif y == "%":
    print(x % z)

else:
    print("Not an expression")