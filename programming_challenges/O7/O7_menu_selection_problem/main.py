import time
import sys

chosen = False
while not chosen:
    try:
        choice = int(input("PLAY GAME(1), instructions(2), quit(3) "))
        if choice == 1:
            print("YOU WIN")
            chosen = True
        elif choice == 2:
            print("Step 1: press 1 to play")
            print("Step 2: win")
            print("PRO TIP: don't press quit")
            print()
        elif choice == 3:
            print("YOU LOSE")
            chosen = True
        else:
            sys.exit()
    except Exception:
        print("You had one job")
        time.sleep(2)
        print("to press a number")
        time.sleep(2)
        print("from 1 to 3")
        time.sleep(2)
        print("and you failed")
        time.sleep(2)
        print("shutting down")
        time.sleep(2)
        sys.exit()
