from dice_roller import DiceRoller

print("\n\nTesting even score ...")
result = DiceRoller.score(2, 4)
if result == 16:
    print("PASS!")
else:
    print("FAIL!!!")

print("\n\nTesting even score with a double ...")
result = DiceRoller.score(2, 2, 5)
if result == 19:
    print("PASS!")
else:
    print("FAIL!!!")


print("\n\nTesting odd score ...")
result = DiceRoller.score(2, 5)
if result == 2:
    print("PASS!")
else:
    print("FAIL!!!")


print("\n\nTesting odd score, lower than 5 ...")
result = DiceRoller.score(2, 1)
if result == 0:
    print("PASS!")
else:
    print("FAIL!!!")
