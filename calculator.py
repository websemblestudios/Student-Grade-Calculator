def calculate_grade(marks):
    percentage = sum(marks) / len(marks)

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    return percentage, grade


marks = [85, 90, 78, 92, 88]

percentage, grade = calculate_grade(marks)

print("Student Grade Calculator")
print("Percentage:", percentage)
print("Grade:", grade)