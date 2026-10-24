#Print grade description using match case


grade = input("Enter grade (A, B, C, D, F): ").upper()

match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Very Good")
    case "C":
        print("Good")
    case "D":
        print("Needs Improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")