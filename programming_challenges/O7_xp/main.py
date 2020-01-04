total_XP = 0
rank = 1

while total_XP < 2000:
    XP = int(input("Enter the XP you earned last game: "))
    total_XP = total_XP + XP
    if total_XP >= 1500 and rank < 5:
        print("You have been promoted to Warrant Officer ")
        rank = 5
    elif total_XP >= 700 and rank < 4:
        print("You have been promoted to Staff Sergeant ")
        rank = 4
    elif total_XP >= 300 and rank < 3:
        print("You have been promoted to Sergeant ")
        rank = 3
    elif total_XP >= 100 and rank < 2:
        print("You have been promoted to Corporal ")
        rank = 2

    print("Total XP: " + str(total_XP))
