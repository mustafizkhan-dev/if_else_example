#Check exam results (Distinction, First Class, Pass, Fail)
    #Assumed grading: Distinction = 75 and above, First Class = 60–74, Pass = 40–59, Fail = below 40.



marks = int(input("Enter marks: "))

if marks >= 75:
    print("Distinction")
elif marks >= 60:
    print("First Class")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")