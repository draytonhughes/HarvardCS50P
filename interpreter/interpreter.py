# Enter the math Questions
# x is an integer
# y is either +, -, *, or /
# z is an integer.

# out put is to be a float at 1 decimal

expression = input("Expression: ")

# convert to variables

a, y, c = expression.split(" ")

x = float(a)
z = float(c)

# Calculate the results

if y == "+":
    output = x + z
    rounded_float = round(output, 1)
    print(rounded_float)

elif y == "-":
    output = x - z
    rounded_float = round(output, 1)
    print(rounded_float)

elif y == "*":
    output = x * z
    rounded_float = round(output, 1)
    print(rounded_float)

elif y == "/":
    output = x / z
    rounded_float = round(output, 1)
    print(rounded_float)

else:
    print("Problem with Expressions")