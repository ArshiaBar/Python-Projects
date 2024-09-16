num1 = float(input("Enter your first value: "))
operator = input("Enter your operator: ")
num2 = float(input("Enter your second value: "))
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
     print(num1 / num2)
else:
    print("invalid operator")

