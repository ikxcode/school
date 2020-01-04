def get_grade_old(marks):
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


def get_grade(mark):
    matched_grade = "U"
    next_grade = ""
    next_mark = -1
    for grade, min_mark in grades.items():
        if mark >= min_mark:
            matched_grade = grade
            break
        else:
            next_grade = grade
            next_mark = min_mark
    next_mark_difference = next_mark - mark
    grade_info = (matched_grade, next_grade, next_mark_difference)
    return grade_info


def readify(grade_info):
    print("You got grade " + str(grade_info[0]))
    if grade_info[0] == list(grades.keys())[0]:
        print("You got the highest grade!")
    else:
        print("The next grade is " + grade_info[1])
        print("To get the next grade, you need " + str(grade_info[2]) + " more marks")


grades = {
    "G9": 80,
    "G8": 67,
    "G7": 54,
    "G6": 41,
    "G5": 31,
    "G4": 22,
    "G3": 13,
    "G2": 4,
    "G1": 2
}


project = ["project: "]
analysis = int(input("How many marks did you get in analysis "))
design = int(input("How many marks did you get in design "))
implementation = int(input("How many marks did you get in implementation "))
evaluation = int(input("How many marks did you get in evaluation "))
project_mark = analysis + design + implementation + evaluation
project.append(project_mark)
project_grade = get_grade(project_mark)
project.append(project_grade)
readify(project_grade)

maths = ["maths: "]
maths_mark = int(input("How many marks did you get in maths? "))
maths.append(maths_mark)
maths_grade = get_grade(maths_mark)
maths.append(maths_grade)
readify(maths_grade)

english = ["english: "]
english_mark = int(input("How many marks did you get in english? "))
english.append(english_mark)
english_grade = get_grade(english_mark)
english.append(english_grade)
readify(english_grade)
