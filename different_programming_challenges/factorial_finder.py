positive = False
number = 0
while not positive:
    try:
        number = int(input("Enter a number and I will find the factorial for it "))
        if number >= 0:
            positive = True
        else:
            print("Sorry I lack the braincells to find factorials of negative numbers. Please enter a positive number")
    except Exception:
        print("That is not an integer, please enter an integer")

found = False
factorial = 1
incrementer = number

while not found:
    if number == 0:
        print("the factorial of 0 is 1")
        found = True
        break

    factorial *= incrementer
    incrementer -= 1

    if incrementer <= 1:
        print("The factorial of " + str(number) + " is " + str(factorial))
        found = True
