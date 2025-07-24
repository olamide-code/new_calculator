# A SIMPLE PYTHON PROGRAMM, THAT IS A CALCULATOR
#A USER WILL INPUT TWO PARAMETERS

running = True
import math
while running:

    user_input  = input("To exit from the program, kindly enter ('q' to quit) or press enter to continue  \n")

    if user_input.lower() == 'q':
        print(" 🙋‍♂️ 🙋‍♂️ Good bye!!! you exited the program")
        break


    try:
        
        number1 = float(input("Kindly enter any number \n"))
        number2 = float(input("Enter your second number \n"))
        operator = input("what operations would you like to perform ('+', '-' , '*' , '/', 'tan' , 'sin', 'cosine') \n")

        if operator == '+':
            result = number1 + number2
            print(f"The result of {number1} + {number2}   is equal to {result}")

        elif operator == '-':
            result = number1 - number2
            print(f"The result of {number1} - {number2} is  {result}")

        elif operator == '*':
            result = number1 * number1
            print(f"The result of {number1} * {number2} is {result}")

        elif operator == '/':
            result = number1/number2
            print(f"the resukt of {number1}/{number2} is {result}")
        
        elif operator == 'sin':
            angle = float(input("Enter your angle"))
            result = math.sin(angle)
            print(f"The result of sin0 is: {result}")


        

        




    except ValueError:
        print("❌❌ Invalid input. Please enter numeric values.")


