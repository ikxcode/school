import random


class Character:
    def __init__(self, name, attack, defence):
        self.name = self.sanitise(name)
        self.attack = attack
        self.defence = defence

    @staticmethod
    def sanitise(name):
        return name.replace("\n", "").strip()


def create_character(name):
    attack = random.randint(0, 100)
    defence = random.randint(0, 100)
    character = Character(name, attack, defence)
    return character


def print_character(character):
    print(character.name)
    print(character.attack)
    print(character.defence)


def write_character_to_file(character):
    character_files = open("character_file.txt", "a")
    character_files.write(character.name)
    character_files.write("\n")
    character_files.write(str(character.attack))
    character_files.write("\n")
    character_files.write(str(character.defence))
    character_files.write("\n")
    character_files.close()


def read_file_and_get_character():
    character_files = open("character_file.txt", "r")
    line = int(input("which character stats do you want to see? (1, 2, 3) "))
    line = line - 1
    line = line * 3
    for x in range(line):
        character_files.readline()
    name = character_files.readline()
    attack = character_files.readline()
    defense = character_files.readline()
    character_4 = Character(name, attack, defense)
    print_character(character_4)


character_1 = create_character("Bob\n")
character_2 = create_character("Kevin")
character_3 = create_character("Stewart")

print_character(character_1)
print_character(character_2)
print_character(character_3)

write_character_to_file(character_1)
write_character_to_file(character_2)
write_character_to_file(character_3)

read_file_and_get_character()
