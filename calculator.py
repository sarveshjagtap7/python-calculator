def add(a, b):
    return a + b

def subtract(a, b):
    x = a - b
    return x

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "error - division by zero"
    return a / b

def main():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number entered")
        return

    op = input("Operation (+ - * /): ").strip()
    if op == '+':
        result = add(num1, num2)
    elif op == "-":
        result = subtract(num1, num2)
    elif op == "*":
        result = multiply(num1, num2)
    elif op == "/":
        result = divide(num1, num2)
    else:
        print("Invalid operation")
        return

    print("Result:", result)

if __name__ == "__main__":
    main()