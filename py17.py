#Check grade based on marks
#Assumed grading: A = 80 and above, B = 60–79, C = 40–59, Fail = below 40.



marks = int(input("Enter marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")