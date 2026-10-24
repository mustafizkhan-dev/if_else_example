#Check whether a student passed all subjects
    #Assumption: Passing marks are 35 in each of three subjects.



m1 = int(input("Enter marks for subject 1: "))
m2 = int(input("Enter marks for subject 2: "))
m3 = int(input("Enter marks for subject 3: "))

if m1 >= 35:
    if m2 >= 35:
        if m3 >= 35:
            print("Passed all subjects")
        else:
            print("Failed in subject 3")
    else:
        print("Failed in subject 2")
else:
    print("Failed in subject 1")