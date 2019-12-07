letters = {}
word = "hello"

for letter in word:
    if letter in letters.keys():
        letters[letter] = letters[letter] + 1
    else:
        letters[letter] = 1

print(letters)
