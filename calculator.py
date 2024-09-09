def add(num1, num2):
    sum = num1 + num2
    return sum

def sub(num1, num2):
    sum = num1 - num2
    return sum

def mul(num1, num2):
    sum = num1 * num2
    return sum

def div(num1, num2):
    sum = num1 / num2
    return sum

def main():
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number "))
    x = add(num1, num2)
    y = sub(num1, num2)
    z = mul(num1, num2)
    w = div(num1, num2)
    print("Addition:", x)
    print("Subtraction:", y)
    print("Multiplication:", z)
    print("Division:", w)
main()