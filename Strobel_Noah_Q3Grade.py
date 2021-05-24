# Name:  Noah Strobel
# Class: GISC-450

# Purpose: This program shows the user student names and numeric grades and asks them to input
# the grades to display the associated letter grades

# Author:  Noah Strobel

# Created: 02/05/2020

################################################################

def main():
    numeric_grades = [100, 99, 85, 71, 60, 49, -22, 102]
    student_list = ['Bobbi', 'Joe', 'Sally', 'Erica', 'Jean', 'Toni', 'Oscar', 'Meyer']
    letter_grades = ['A', 'B', 'C', 'D', 'F', 'invalid']

    print("Students' numeric grades are as follows: \nBobbi: 100\nJoe: 99\nSally: 85\nErica: 71\
          \nJean: 60\nToni: 49\nOscar: -22\nMeyer: 102")

    student = input("Enter a student's name to display their letter grade: ")
    grade = int(input("Enter the student's numeric grade (numbers only): "))

################################################################

    print("---Valid grades---")
    print("Name:    Numeric grade:    Letter grade:")

    while student != "Quit" or 'quit':
        if student == "Bobbi" or "bobbi" and grade == 100:
            print(f"Bobbi {numeric_grades[0]:>10} {letter_grades[0]:>15}")
            break
        elif student == "Joe" or "joe" and grade == 99:
            print(f"Joe {numeric_grades[1]:>10} {letter_grades[0]:>15}")
            break
        elif student == "Sally" or "sally" and grade == 85:
            print(f"Sally {numeric_grades[2]:>10} {letter_grades[1]:>15}")
            break
        elif student == "Erica" or "erica" and grade == 71:
            print(f"Erica {numeric_grades[3]:>10} {letter_grades[2]:>15}")
            break
        elif student == "Jean" or "jean" and grade == 60:
            print(f"Jean {numeric_grades[4]:>10} {letter_grades[3]:>15}")
            break
        elif student == "Toni" and "toni" or grade == 49:
            print(f"Toni {numeric_grades[5]:>10} {letter_grades[4]:>15}")
            break

        else:
            print("\n---Invalid grades---")
            print("Name       Numeric grade")

        if student == "Oscar" or "oscar" and grade == -22:
            print(f"Oscar {numeric_grades[6]:>10}")
            break
        elif student == "Meyer" or "meyer" and grade == 102:
            print(f"Meyer {numeric_grades[7]:>10}")
            break
        if student not in student_list or grade not in numeric_grades:
            print("\n---Please enter a student name or grade contained within the list---")
            break




if __name__ == '__main__':
    main()
