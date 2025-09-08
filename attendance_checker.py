number_of_classes=int(input("Enter the number of classes held: "))
number_of_classes_attended=int(input("Enter the number of classes attended: "))
attendance_percentage=(number_of_classes_attended/number_of_classes)*100
if number_of_classes == 0: print("this is not possible")
if attendance_percentage >= 75:
    print("You are allowed to sit in the exam.")
else:
    print("You are not allowed to sit in the exam.")
