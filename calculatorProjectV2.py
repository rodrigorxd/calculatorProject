"""
Rodrigo Drumond Valente
First Python project - Simple Calculator.

Using conditional statements, booleans, loops, flags.
03/17/2023 - mm/dd/yyyy.

Using conditional statements, booleans, loops, flags, math(built-in function), functions, modules
03/31/2023 - mm/dd/yyyy
"""
from operations import *

finish = False

while not finish:
    option = int(input("\t----MENU----\n0 - How to use\n1 - Sum\n2 - Subtraction\n3 - Division\n4 - Multiplication\n"
                       "5 - Exponentiation\n6 - Percentage\n7 - Bhaskara\n8 - Square root\n9 - Quit\n\nSelect an option:"))
    if option >= 0 and option <= 9:
        if option == 0:
            result = f"{howToUse()}"
        elif option <= 7:
            first_number = float(input("Type the first number:"))
            second_number = float(input("Type the second number:"))
            if option == 1:
                sum_result = sum(first_number,second_number)
                result = f"{first_number} + {second_number} = {sum_result}"
            elif option == 2:
                subtraction_result = subtraction(first_number,second_number)
                result = f"{first_number} - {second_number} = {subtraction_result}"
            elif option == 3:
                validation = validateNumber(second_number, option)
                if validation == True:
                    division_result = division(first_number, second_number)
                    result = f"{first_number} / {second_number} = {division_result}"
                else:
                    result = "Divisor(second number typed) can't be zero"
            elif option == 4:
                multiplication_result = multiplication(first_number, second_number)
                result = f"{first_number} x {second_number} = {multiplication_result}"
            elif option == 5:
                exponentiation_result = exponentiation(first_number, second_number)
                result = f"{first_number} ^ {second_number} = {exponentiation_result}"
            elif option == 6:
                percentage_result = percentage(first_number, second_number)
                result = f"{first_number}% of {second_number} = {percentage_result}"
            elif option == 7:
                third_number = float(input("Type the third number (c):"))
                validation = validateNumber(first_number, option)
                if validation == True:
                    roots = bhaskara(first_number, second_number, third_number)
                    result = f"Roots: {roots[0]} , {roots[1]}"
                else:
                    result = "First number (axˆ2) can't be zero"
        elif option == 8:
            first_number = float(input("Type the number:"))
            validation = validateNumber(first_number, option)
            if validation == True:
                square_result = squareRoot(first_number)
                result = f"Square root of {first_number}: {square_result}"
            else:
                result = "No real root for square root of negative numbers"
        else:
            finish = True
            result = "Program finished!"
    else:
        result = "Invalid option, please try again!"
    print(result)
