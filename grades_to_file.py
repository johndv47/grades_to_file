try:
    # Creates grades.txt in CWD and interacts in write mode.
    with open("grades.txt", mode="w") as file:
        grade = int(input("Enter grade, -1 to end: "))  # get one grade

        # While loop checks for sentinel value input
        while grade != -1:
            # Grade is written to the file (grades.txt)
            file.write(str(grade) + "\n")

            # Prompts user again for input
            grade = int(input("Enter grade, -1 to end: "))

        else:
            print(
                "\nAll entered grades were saved to grades.txt file in your current directory."
            )

# Error handling - verifies user input is only digits.
except ValueError:
    print("\nPlease enter only digits.")
