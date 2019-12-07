def run_adder_problem():
    print("running adder problem")
    num1 = get_number_input("Lets add numbers! Number 1?")
    num2 = get_number_input("Number 2?")
    total = num1 + num2
    print("The sum of these numbers is " + str(total))


def run_height_and_weight_problem():
    print("running height and weight problem")
    height = get_number_input("please enter your height in inches: ")
    weight = get_number_input("please enter your weight in stones: ")
    height = height * 2.54
    weight = weight * 6.634
    print("Your height is " + str(height) + "cm and your weight is " + str(weight) + "kg")


def run_circle_properties_problem():
    print("running circle properties problem")
    diameter = get_number_input("Enter the diameter of the circle")
    arc_angle = get_number_input("Enter the arc angle")
    radius = diameter / 2
    area = 3.14 * radius * radius
    circumference = diameter * 3.14
    arc_length = circumference * arc_angle / 360
    print("The radius is " + str(radius))
    print("The area is " + str(area))
    print("The circumference is " + str(circumference))
    print("The arc length is " + str(arc_length))


def get_number_input(prompt):
    while True:
        try:
            number = input(prompt)
            return int(number)
        except:
            print("Please enter a valid input")



def check_choice(user_choice):
    try:
        return int(user_choice)
    except:
        return -1

def choose_option():
    choice = -1
    while choice != 0:
        print("What would you like to do: ")
        print("1) Adder")
        print("2) Height and Weight")
        print("3) Circle Properties")
        choice = check_choice((input("Please select: 1, 2, 3, or 0 to exit ")))
        if choice == 1:
            print()
            run_adder_problem()
        elif choice == 2:
            print()
            run_height_and_weight_problem()
        elif choice == 3:
            print()
            run_circle_properties_problem()
        elif choice == 0:
            break
        else:
            print("Please enter a valid option")


choose_option()
