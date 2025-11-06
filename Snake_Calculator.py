"""
Snake Calculator
v1.51
By Lakshya
"""


#----------functions---------

def calculate_sine():
    import math
    try:
        angle_degrees = float(input("Enter an angle in degrees to find its sine: "))
        angle_radians = math.radians(angle_degrees)
        sine_result = math.sin(angle_radians)
        print(f"The sine of {angle_degrees} degrees is: {sine_result}")
    except ValueError:
        print("Invalid input. Please enter a numerical value for the angle.")

    # You can call this function within your main calculator loop or directly
    calculate_sine()
def ForArith():
    mathProblemnums = int(input('How many numbers do you want in your equation? '))
    Operators()
    mathProblemOp = str(input("What operator would you like me to use? "))
    if mathProblemOP == "/":
        print("Ok!")
    elif mathProblemOP == "*":
        print("Ok!")
    elif mathProblemOP == "-":
        print("Ok!")
    elif mathProblemOP == "+":
        print("Ok!")
    else:
        Invalid()
        
def Invalid():
    print("Input is Invalid. Please try again.")
def Operators():
    print("addition = +")
    print("subtraction = -")
    print("multiplication = *")
    print("division = /")
def AnswerIs():
    print("The answer is...")
def emptyLine():
    print()
def again():
    import math
    import time
    arithnum = 0
    name = input("What's your name? ")
    print('Hello, ' + name + '!')
    time.sleep(0.47567)
    print('Welcome to to the snake calculator!')
    time.sleep(0.376786777777777777887669814)
    print('How may I help you today? ')
    print('The following is case sensitive.')
    emptyLine()
    time.sleep(0.67)
    print('Please write your choice as a number from 1-13, determined by the order of the following')
    print("1 - Arithmetic (Still trying to find out how to do division here)")
    print("2 - square root")
    print("3 - exponents")
    print("4 - Fraction to Decimal Conversion")
    print('5 - cube root ')
    print("6 - abs value")
    print("7 - factorial")
    print("8 - logarithm")
    print("9 - Floor Division")
    print("10 - area (Square, Triangle)")
    print("11 - perimeter")
    print("12 - sine")
    print("13 - triangle angles")
    print("14 - Greatest Common Factor")
    print("15 - equations (one-variable)")
    while True:
        try:
            choice = int(input("Please enter your number "))
            break
        except ValueError:
            Invalid()
    if choice == 1:
        print('Ok!')
        print()
        while True:
            try: 
                mathProblemnums = int(input('How many numbers do you want in your equation? '))
                Operators()
                mathProblemOp = str(input("What operator would you like me to use? "))
                if mathProblemOp == "/":
                    print("Ok!")
                    break
                elif mathProblemOp == "*":
                    print("Ok!")
                    break
                elif mathProblemOp == "-":
                    print("Ok!")
                    break
                elif mathProblemOp == "+":
                    print("Ok!")
                    break
                else:
                    Invalid()
                    ForArith
                
            except ValueError:
                Invalid()
        for i in range(mathProblemnums):
            while True:
                if mathProblemOp == "+":
                    try:
                        anum = int(input(f"Enter number {i + 1}: "))
                        arithnum += anum
                        break
                    except ValueError:
                        Invalid()
                elif mathProblemOp == "-":
                    try:
                        anum = int(input(f"Enter number {i + 1}: "))
                        arithnum -= anum
                        break
                    except ValueError:
                        Invalid()
                elif mathProblemOp == "*":
                    try:
                        anum = int(input(f"Enter number {i + 1}: "))
                        arithnum *= anum
                        break
                    except ValueError:
                        Invalid()    
                elif mathProblemOp == "/":
                    try:
                        current_value = current_value / divisor  # Divide and reassign
                        print(f"Current value: {current_value}")
                    # TRY TO FIND HOW TO ADD DIVISION.                      wwwwwwwwwwww
                    #above is ai. i dont think it works. keep trying.
                    
                        AnswerIs()
                        print(str(arithnum) + "!")
                    except ValueError:
                        Invalid()

        
    elif choice == 2:
        square_root = int(input('What number would you like me to get the square root of? '))
        square_root2 = str(math.sqrt(square_root))
        print(square_root2 + ' is the square root of ' + str(square_root))
    elif choice == 3:
        exponents = int(input('What number would to like me to find the ___ power of? '))
        exponents2 = int(input('What power would you like me to raise your number to? '))
        emptyLine()
        emptyLine()
        print(exponents ** exponents2, " is your answer!")
        time.sleep(2)
    elif choice == 4:
        F_to_Dnum = input('numerator? ')
        F_to_Dden = input("Denominator? ")
        print(int(F_to_Dnum)/int(F_to_Dden))
        print(" ")
        print("answer is above!")
        
        print(F_to_DAns + ' Is the decimal equivalent of ' + F_to_D)
    elif choice == 5:
        croot = float(input("What number would you like me to get the cube root of? "))
        emptyLine()
        emptyLine()
        print("The cube root of " + str(croot) + "is...")
        print(croot ** (1 / 3))
    elif choice == 6:
        emptyLine()
        absval = int(input("What would you like the absolute value of? "))
        print("the absolute value of " + str(absval) + " is " + str(abs(absval) + "!"))
    elif choice == 7:
        emptyLine()
        factorialvalue = input("what number would you like me to get the factorial of? ")
        print("The facotrial of " + str(factorialvalue) + " is...")
        emptyLine()
        emptyLine()
        print(math.factorial(int(factorialvalue)))
    elif choice == 8:
        emptyLine()
        logbase = input("what is the base of your logarithm? ")
        logexpo = input("what is the exponent of your logarithm? ")
        print("the anser to your logarithm with base " + str(logbase) + " and exponent " + str(logexpo) + " is...")
        print(math.log(int(logexpo), int(logbase)))
    elif choice == 9:
        emptyLine()
        print("So you have chosen floor division.")
        print("If you didn't know, floor division is")
        print("just division, but rounding down to")
        print("a whole number.")
        floordivend = int(input("What is the dividend? "))
        floordivisor = int(input("What is the divisor? "))
        print("Your answer is...")
        print(".")
        time.sleep(0.54)
        print(".")
        print(floordivend//floordivisor)
    elif choice == 10:
        while True:
            shape = input("Square or Triangle? ")
            if shape == "Square":
                try:
                    squ_sides = int(input("what is the side length of the square? "))
                    print(squ_sides * squ_sides)
                    print("The answer is above!")
                    break
                except ValueError:
                    Invalid()
            elif shape == "square":
                while True:
                    try:
                        squ_sidesl = int(input("what is the side length of the square?"))
                        print(squ_sidesl * squ_sidesl)
                        print("The answer is above!    ")
                        break
                    except ValueError:
                        Invalid()
                    
            elif shape == "triangle":
                while True:
                    try:
                        basetri = int(input("base? "))
                        heighttri = int(input("height? "))
                        bplush = basetri * heighttri
                        triarea = bplush / 2
                        AnswerIs()
                        print(str(triarea))
                        break
                    except ValueError:
                        Invalid() 
            elif shape == "Triangle":
                while True:
                    try:
                        basetri = int(input("base? "))
                        heighttri = int(input("height? "))
                        bplush = basetri * heighttri
                        triarea = bplush / 2
                        AnswerIs()
                        print(str(triarea))
                        break
                    except ValueError:
                        Invalid()
    elif choice == 11 :
        while True:
            try:    
                sidescount = int(input("how many sides does your shape have? "))
                sidesunit = str(input("what unit would you like me to use?"))
                break
            except ValueError:
                Invalid()
        perimeter = 0
        for guysyallneedtostopwiththe67brainrotitssoweirsandweneedtofixtheworldandlucianogetoffrobloxpleaseyourelectricitybillissocookedman in range(sidescount):
            while True:
                try:
                    num = int(input(f"Enter side number {guysyallneedtostopwiththe67brainrotitssoweirsandweneedtofixtheworldandlucianogetoffrobloxpleaseyourelectricitybillissocookedman + 1}: "))
                    perimeter += num
                    break
                except ValueError:
                    Invalid()
        AnswerIs()
        print(str(perimeter) + sidesunit + "!")
    elif choice == 12:
        calculate_sine()
    elif choice == 13:
        print("Give me two angles of a triangle and i will give you the third one.")
        while True:
            try:
                randangle1 = int(input("Enter side number 1: "))
                randangle2 = int(input("Enter side number 2: "))
                break
            except ValueError:
                print("Sorry, invalid input")
        calcangle = randangle1 + randangle2
        thirdangle = 180 - calcangle
        print("The third angle is...")
        time.sleep(0.4)
        print(str(calcangle) + '°!')    
    elif choice == 14:
        print("Greatest Common Factor = GCF")
        firstgcf = input("What is the first number you would like to get the GCF of? ")
        secgcf = input("what is your second number? ")
        import math

# Calculate the GCF (GCD)
        gcf_value = math.gcd(int(firstgcf), int(secgcf))

# Print the result
        

        print("The result of the GCF of " + firstgcf + " and " + secgcf + " is..")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(str(gcf_value) + "!")
   # elif choice == 15:
    #    print("This took me langer than it shouldve.")
     #   equation = input(" WHat is the equation?")
      # to be coming soon  
    elif choice == 67:
        print("6-6-6-6-6-6-7-7-- SIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENvSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVENSIX SEVEN SIX SEVEN")
        quit()
    elif choice == 21:
        print("I would be very good friends with you lol")
    else:
        print("what you have entered has not been added yet, is invalid, or has a typo. Please try again. Thank you.")
        again()

    time.sleep(1.3141592653859)
    emptyLine()
    emptyLine()
    calcagain = input("Wanna use this program again? (Y/N) ")
    if calcagain == "Y" or calcagain == "y":
        again()
    elif calcagain == "n" or calcagain == "N":
        print('Thank you for using snake calculator, ' + name + '! I wish you a great day!')

#----------main script---------


again()


