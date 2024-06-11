# Print a welcome message to the console
print("Welcome to Students' Grades Calculator! \n")

# Dictionary storing students' names as keys and their scores as values
students_scores = {
    "Zaki": 99,
    "Ali": 87,
    "Zahra": 88,
    "Maliha": 79,
    "Zohal": 67,
    "Rahman": 73
}

# Dictionary to store students' names as keys and their corresponding grades as values
students_grades = {}

# Loop through each student in the students_scores dictionary
for student in students_scores:
    # Get the score of the current student
    score = students_scores[student]

    # Determine the grade based on the score
    if score > 90:
        students_grades[student] = "Outstanding"      # Assign "Outstanding" if the score is greater than 90
    elif score > 80:
        students_grades[student] = "Exceeds Expectation"  # Assign "Exceeds Expectation" if the score is greater than 80
    elif score > 70:
        students_grades[student] = "Acceptable"       # Assign "Acceptable" if the score is greater than 70
    else:
        students_grades[student] = "Fails"            # Assign "Fails" if the score is 70 or below

# Print the final students_grades dictionary to the console
print(students_grades)
