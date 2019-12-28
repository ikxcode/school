# this program checks the length of gamertags entered

valid_gamertag = True

while valid_gamertag:
    print("Gamertags must be less than 15 characters")
    gamertag = input("Enter your gamertag ")
    gamertag_length = len(gamertag)
    if gamertag_length > 15:
        print("Your gamertag is too long")
    else:
        print("Gamertag accepted")
        valid_gamertag = False
