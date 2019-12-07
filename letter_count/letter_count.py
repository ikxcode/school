letters = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l",
           "z", "x", "c", "v", "b", "n", "m", ]

word = input("Enter a word: ")

for j in letters:
    count = word.count(j)
    if count > 0:
        print("This word has the letter " + j + " in it " + str(count) + " times")
