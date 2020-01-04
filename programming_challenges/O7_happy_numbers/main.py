

def run_happy_numbers_problem():
    is_recurring = False
    is_happy = False
    number = get_user_input()
    number_str = number
    while not is_recurring and not is_happy:
        digit_list = split_number_into_digits(number_str)
        squared_list = square_digits(digit_list)
        sum_of_digits = sum_digits(squared_list)
        number_str = str(sum_of_digits)
        is_recurring = is_number_recurring(sum_of_digits)
        is_happy = is_number_happy(sum_of_digits)

    if is_recurring:
        print("the number " + number + " is sad")
    elif is_happy:
        print("the number " + number + " is happy")


def get_user_input():
    while True:
        try:
            number = input("Give me a positive integer and I will check if it is happy or sad: ").strip()
            if int(number) <= 0:
                print("That is not a positive integer")
            else:
                return number
        except Exception:
            print("That is not a positive integer")


def split_number_into_digits(number):
    digit_list = []
    for digit in number:
        digit_int = int(digit)
        digit_list.append(digit_int)
    return digit_list


def square_digits(digit_list):
    squared_list = []
    for digit in digit_list:
        squared_digit = digit * digit
        squared_list.append(squared_digit)
    return squared_list


def sum_digits(squared_list):
    sum = 0
    for digit in squared_list:
        sum += digit
    return sum


def is_number_recurring(number):
    return number == 4


def is_number_happy(number):
    return number == 1


run_happy_numbers_problem()
