# Name:    Noah Strobel
# Class    GISC-450 Spring 2021

# Purpose: Displays the letter grade for scores between 0-100 using a for loop
# If the grade within the list is >= 101 or < 0, the output will display the grade and that it is invalid

# Author:  Noah Strobel

# Created:    02/04/2021

################################################################

def main():

    grades = [100, 99, 85, 71, 60, 49, -22, 102]
    for grade in grades:
        if grade > 100:
            print(f"A grade of {grade} is invalid")
        elif grade >= 90:
            print(f"A grade of {grade} is an A")
        elif grade >= 80:
            print(f"A grade of {grade} is a B")
        elif grade >= 70:
            print(f"A grade of {grade} is a C")
        elif grade >= 60:
            print(f"A grade of {grade} is a D")
        elif grade >= 0:
            print(f"A grade of {grade} is an F")
        elif grade < 0:
            print(f"A grade of {grade} is invalid")


if __name__ == '__main__':
    main()

print("\n---First grade program finished---")
# The program has looped through all grades within the list and is now complete
