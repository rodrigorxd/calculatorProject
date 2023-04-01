import math

#Tutorial on how to use calculator functions and its format
def howToUse():
    print("\nHow to use:\n\n-Decimals: replace comma (,) with do dot (.) - Ex:Decimals (5.6)\n-Division: the second number"
          "(divisor) can't be 0\n-Exponentiation: format (first_number ^ second_number)\n-Percentage: "
          "format (first_number % of second_number) - Ex: 5% of 100\n-Square Root: Type just one POSITIVE number (radicand)\n"
          "-Bhaskara: First number (a) can't be zero - format (first_number = a; second_number = b; third_number =c)")

#Validate numbers (some operations can proceed with zero as first number typed or if a negative number is typed)
def validateNumber(number, choice):
    if choice == 8:
        if number < 0:
            return False
        else:
            return True
    elif number == 0:
        return False
    else:
        return True

#Sum
def sum(first, second):
    return first + second
#Subtraction
def subtraction(first, second):
    return first - second
#Division
def division(first, second):
    return first / second
#Multiplication
def multiplication(first, second):
    return first * second
#Exponentiation
def exponentiation(first, second):
    return first ** second
#Percentage
def percentage(first, second):
    return ((first / 100) * second)
#Bhaskara
def bhaskara(first, second, third):
    delta = (second ** 2) - (4 * first * third)
    if delta < 0:
        print("No real roots.")
        roots = ["-", "-"]
    elif delta == 0:
        root = (((-second) + math.sqrt(delta)) / (2 * first))
        roots = [root, root]
    else:
        root_one = (((-second) + math.sqrt(delta)) / (2 * first))
        root_two = (((-second) - math.sqrt(delta)) / (2 * first))
        roots = [root_one, root_two]
    return roots
#Square root
def squareRoot(first):
    return math.sqrt(first)
