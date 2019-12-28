def ask_user_for_bank_amounts(question):
    while True:
        try:
            number = int(input(question))
            if number > 0:
                return number
            else:
                print("just give me a positive integer")
        except Exception:
            print("just give me a positive integer")


current_balance = ask_user_for_bank_amounts("How much money have you put in your savings account? ")
interest_rate = ask_user_for_bank_amounts("What is the interest rate (AER) ? ")
desired_balance = ask_user_for_bank_amounts("How much money do you want in your savings account? ")

years = 0
interest_rate = interest_rate / 100
while current_balance < desired_balance:
    years += 1
    current_balance = current_balance + (current_balance * interest_rate)
    print("year " + str(years) + ": " + str(current_balance))

print(str(years) + " years needed to reach desired balance")
