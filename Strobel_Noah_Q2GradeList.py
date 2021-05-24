# Name:     Noah Strobel
# Class:    GISC-450 Spring 2021

# Purpose:  This program displays numeric grades and their corresponding letter grades in two columns
# Additionally, it displays the highest and lowest numeric grades and the most frequent letter grade
# No numeric grades are represented more than once

# Author:  Noah Strobel

# Created:  02/04/2021


#########################################################

def main():
    numeric_variable = "Numeric grade"
    letter_variable = "Letter grade"
    grades = [100, 99, 85, 71, 60, 49, -22, 102]
    letter_grades = ['A', 'B', 'C', 'D', 'F', 'invalid']
    print(f"{numeric_variable:20} {letter_variable:10}")

    for grade in grades:
        if grade > 100:
            print(f"{grade} {letter_grades[5]:>20}")
        elif grade >= 90:
            print(f"{grade} {letter_grades[0]:>20}")
        elif grade >= 80:
            print(f"{grade} {letter_grades[1]:>20}")
        elif grade >= 70:
            print(f"{grade} {letter_grades[2]:>20}")
        elif grade >= 60:
            print(f"{grade} {letter_grades[3]:>20}")
        elif grade >= 0:
            print(f"{grade} {letter_grades[4]:>20}")
        elif grade < 0:
            print(f"{grade} {letter_grades[5]:>20}")

#########################################################
    print(f"\n\n\tThe highest numeric grade is {max(grades)}")
    print(f"\tThe lowest numeric grade is {min(grades)}")
    print(f"\tThe highest letter grade is {max(letter_grades)}")
    print(f"\tThe lowest letter grade is {letter_grades[5]}")

    # The highest and lowest grades are both invalid, so for the valid ones:

    print(f"\n\tThe highest valid numeric grade is {grades[0]}")
    print(f"\tThe highest valid letter grade is {letter_grades[0]}")
    print(f"\n\tThe lowest valid numeric grade is {grades[5]}")
    print(f"\tThe lowest valid letter grade is {letter_grades[4]}")

    # This should return the most frequent grades in their respective categories:

    def most_frequent(letter_grades):
        return max(set(letter_grades), key=letter_grades.count)

    print(f"\n\tThe most frequent valid letter grade is {most_frequent(letter_grades[0])}")
    print("\tThere are no numeric grades represented more than once")


if __name__ == '__main__':
    main()

    print("\n\t---Second grade program finished---")
