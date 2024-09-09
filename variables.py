def variable_practice():
    year = 12
    age_in_months = int(input("Whats your age: "))
    print("Your age in months is:", age_in_months * year)
    month = 30
    days_in_year = int(year * month)
    print("The number of days in a year is:", (month * year)+5)
    name_of_first_pet = str = "Leo"
    print("The name of your first pet:", name_of_first_pet)
    first_five_digits_pi = float(22/7)
    print("The first five digits of Pi:", first_five_digits_pi)

def expressions_practice():
    x = 4
    y = 8
    z = 12
    literal = 'string1'
    add = x + y
    exponent = x**y
    floordiv = x//y
    mod = x%y
    paranthesis = (x+y)*x
    operators = (y - z)//x**z
    print(literal)
    print(add)
    print(exponent)
    print(floordiv)
    print(mod)
    print(paranthesis)
    print(operators)

def prompt_and_print():
    num1 = float(input("Number 1 is "))
    num2 = float(input("Number 2 is "))
    addition = int(num1) + int(num2)
    subtraction = int(num1)-int(num2)
    multiplication = int(num1) * int(num2)
    division = int(num1) / int(num2)
    print("Addition:", addition)
    print("Subtraction:", subtraction)
    print("Multiplication:", multiplication)
    print("Division:", division)

def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()
main()
