#Print result status using match case


status = input("Enter result status (pass/fail/absent): ").lower()

match status:
    case "pass":
        print("Congratulations! You passed.")
    case "fail":
        print("You did not pass.")
    case "absent":
        print("You were absent for the exam.")
    case _:
        print("Invalid result status")