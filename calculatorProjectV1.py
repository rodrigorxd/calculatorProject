"""
Rodrigo Drumond Valente
First Python project - Simple Calculator (without built-in functions, such as sqrt()).
Using conditional statements, booleans, loops, flags.
03/17/2023 - mm/dd/yyyy.
"""

#continue or not flag
flag = True

#loop (calculator structure)
while flag:
    #menu
    choice = int(input("**** Menu ****\n\n0 - Quit\n1 - Sum\n2 - Subtraction\n3 - Division\n4 - Multiplication\n5 - Exponentiation"
                       "\n6 - Percentage\n7 - Square Root\n\nChoose an option:"))
    #out of range
    if (choice < 0) or (choice > 7):
        result = "Invalid choice!"
    #quit program
    elif choice == 0:
        result = "Program finished."
        flag = False
    #calculator functions
    elif (choice >= 1) and (choice <= 6):
        firstNumber = float(input("Type the first number:"))
        secondNumber = float(input("Type the second number:"))
        #sum
        if choice == 1:
            sum = firstNumber + secondNumber
            result = f"Sum: {sum}"
        #subtraction
        elif choice == 2:
            subtraction = firstNumber - secondNumber
            result = f"Subtraction: {subtraction:.2f}"
        #Division
        elif choice == 3:
            #Zero as divisor treatment
            if secondNumber == 0:
                result = "Divisor can't be zero."
            else:
                division = firstNumber / secondNumber
                result = f"Division: {division:.2f}"
        #Multiplication
        elif choice == 4:
            multiplication = firstNumber * secondNumber
            result = f"Multiplication: {multiplication:.2f}"
        #Exponentiation
        elif choice == 5:
            exponentiation = firstNumber ** secondNumber
            result = f"Exponentiation({firstNumber}ˆ{secondNumber}): {exponentiation}"
        #Percentage
        else:
            percentage = (firstNumber / 100) * secondNumber
            result = f"Percentage({firstNumber}% of {secondNumber}): {percentage}"
    #Square root
    elif choice == 7:
        #As square root, it receives from input only one number
        firstNumber = float(input("Type the number:"))
        #Square root of 0 treatment
        if firstNumber < 0:
            result = "No square root for negative numbers"
        else:
            squareRoot = firstNumber ** 0.5
            result = f"Square root: {squareRoot}"
    print(result)
