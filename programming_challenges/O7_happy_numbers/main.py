import sys


def split_number_into_digits(number_int):
    check_for_sad_number(number_int)
    check_for_happy_number(number_int)
    number_str = str(number_int)
    digit_list = []
    for digit in number_str:
        digit = int(digit)
        digit_list.append(digit)
    square_digits(digit_list)


def square_digits(digit_list):
    squared_list = []
    for digit in digit_list:
        squared_digit = digit * digit
        squared_list.append(squared_digit)
    add_digits(squared_list)


def add_digits(squared_list):
    added_digit = 0
    for digit in squared_list:
        added_digit = added_digit + digit
    # clear_lists()
    split_number_into_digits(str(added_digit))


def check_for_sad_number(added_digit):
    if added_digit == "4":
        print("The number " + str(number) + " is sad")
        sys.exit()


def check_for_happy_number(added_digit):
    if added_digit == "1":
        print("The number " + str(number) + " is happy")
        sys.exit()


number = input("Give me a number and I will check if it is a happy number or not: ")
split_number_into_digits(number)
