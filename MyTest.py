# Calculator code created by m4zbro

# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y

# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print("Result of addition:", add(num1, num2))
elif choice == '2':
    print("Result of subtraction:", subtract(num1, num2))
elif choice == '3':
    print("Result of multiplication:", multiply(num1, num2))
elif choice == '4':
    print("Result of division:", divide(num1, num2))
else:
    print("Invalid choice")
