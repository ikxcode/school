

# Scenario 1

# task 1
heroes = ["Batman", "Wonder Woman", "Superman", "Spiderman"]

# task 2
print("Current pilot: ", heroes[0])

# task 3
print("Current Co-Pilot: ", heroes[1])

# task 4
heroes[2] = "Hit Girl"

# task 5
heroes.append("Antman")
heroes.append("Captain Marvel")

# task 6
print(heroes)

# extension task
try:
    hero_fired = int(input("Pick a number from 0 to 5 to replace a hero: "))

    if 0 <= hero_fired <= 5:
        new_hero = input("What hero do you choose as a replacement? ")
        heroes[hero_fired] = new_hero
        print(heroes)
    else:
        print("That wasn't a number between 0 and 5...")

except Exception:
    print("That was not an integer...")


# Scenario 2

# task 1
villains = ["The Joker", "Magneto", "Red mist", "Doc Ock"]

# task 2
for counter in range(4):
    print(villains[counter])

# task 3
villain_wages = [21, 17, 3, 5]

# task 4
for counter in range(4):
    print(villains[counter], ": £", villain_wages[counter], "million")

# task 5
total_wage = 0
for wage in villain_wages:
    total_wage += wage
print("Total Wage : £ " + str(total_wage) + " million")
