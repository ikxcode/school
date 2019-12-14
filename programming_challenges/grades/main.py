def get_grade(marks):
    if marks >= 80:
        return "G9"
    elif marks >= 67:
        return "G8"
    elif marks >= 54:
        return "G7"
    elif marks >= 41:
        return "G6"
    elif marks >= 31:
        return "G5"
    elif marks >= 22:
        return "G4"
    elif marks >= 13:
        return "G3"
    elif marks >= 4:
        return "G2"
    elif marks >= 2:
        return "G1"
    else:
        return "U"


results = []

maths = ["maths: "]
maths_mark = int(input("How many marks did you get in maths? "))
maths.append(maths_mark)
maths_grade = get_grade(maths_mark)
maths.append(maths_grade)
results.append(maths)

english = ["english: "]
english_mark = int(input("How many marks did you get in english? "))
english.append(english_mark)
english_grade = get_grade(english_mark)
english.append(english_grade)
results.append(english)

print(results)
