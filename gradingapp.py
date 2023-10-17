
print("\n\tWELCOME TO OUR GRADING APP")
grade = int(input("Please enter your grade to calculate: "))

if(grade >= 80 and grade <= 100):
    print("your grade is A (Distinction)")
elif(grade >= 60 and grade <= 79):
    print("Your grade is B (Excelent)")
elif(grade >= 45 and grade <= 59):
    print("Your grade is C (Credit)")
elif(grade >= 20 and grade <= 44):
    print("Your grade is PASS")
elif(grade >= 0 and grade <= 19):
    print("oops! you failed this course. try again next year")
else:
    print("invalid entry, please enter a grade from 1 to 100")
