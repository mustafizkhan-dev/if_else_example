#Check whether a student is eligible for an exam (attendance + marks)
    #Assumption: Attendance must be at least 75% and marks must be at least 40.



attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter marks: "))

if attendance >= 75:
    if marks >= 40:
        print("Eligible for exam")
    else:
        print("Not eligible: Low marks")
else:
    print("Not eligible: Low attendance")