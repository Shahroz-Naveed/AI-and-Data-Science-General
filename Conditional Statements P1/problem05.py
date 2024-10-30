# 05 Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
# 80+-> A+, (70-80)-> A, (60-70)->B, (50-60)-> C, (40-50)->D, (<40)->F
grade_percentage = int(input("Enter a grade percentage to get corresponding grade : "))
if grade_percentage > 80:
    print("Your grade is A+ ")
elif grade_percentage <= 80 and grade_percentage >= 70:
    print("Your grade is A")
elif grade_percentage <= 70 and grade_percentage >= 60:
    print("Your grade is B")
elif grade_percentage <= 60 and grade_percentage >= 50:
    print("Your grade is C")
elif grade_percentage <=50 and grade_percentage >= 40:
    print("Your grade is D")
elif grade_percentage <40 and grade_percentage >= 0:
    print("Your grade is F")
else:
    print("Invalid grade percentage. Please enter a number between 0 and 100.")