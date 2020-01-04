import sys

digit_list = []
squared_list = []


number = input("Give me a number and I will check if it is a happy number or not: ")


def split_number_into_digits(number):
    check_for_sad_number(number)
    check_for_happy_number(number)
    number = str(number)
    for digit in number:
        digit = int(digit)
        digit_list.append(digit)
    square_digits()


def square_digits():
    for digit in digit_list:
        squared_digit = digit * digit
        squared_list.append(squared_digit)
    add_digits()


def add_digits():
    added_digit = 0
    for digit in squared_list:
        added_digit = added_digit + digit
    clear_lists()
    split_number_into_digits(str(added_digit))


def clear_lists():
    digit_list.clear()
    squared_list.clear()


def check_for_sad_number(added_digit):
    if added_digit == "4":
        print("The number " + str(number) + " is sad")
        sys.exit()


def check_for_happy_number(added_digit):
    if added_digit == "1":
        print("The number " + str(number) + " is happy")
        sys.exit()


split_number_into_digits(number)
