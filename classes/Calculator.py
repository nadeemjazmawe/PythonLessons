def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

value = input("Enter Choice: ")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if value == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif value == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

elif value == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif value == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

