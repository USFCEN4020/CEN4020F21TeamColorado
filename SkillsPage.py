import Error

# main function, menu for Skills
def skillsMenu():
    while True:
        print("              Skills               ")
        print("Please select one of the following options")
        print("""
            1. Learn about Scrum/Agile workflow
            2. Learn how to program in Python
            3. Learn how to test code using PyTest
            4. Learn how to use external libraries such as SQL, NumPy, and more in Python
            5. Learn how to create a professional portfolio and resume
            6. Back to home page
            """)
        try:
            e = Error()
            newOption = int(input("Choice: "))
            print('\n')
            # Skill 1 option
            if newOption == 1:
                e.underConstruction()
            # Skill 2 option
            elif newOption == 2:
                e.underConstruction()
            # Skill 3 option
            elif newOption == 3:
                e.underConstruction()
            # Skill 4 option
            elif newOption == 4:
                e.underConstruction()
            # Skill 5 option
            elif newOption == 5:
                e.underConstruction()
            # Return home option
            elif newOption == 6:
                print("Returning to home page...")
                break
        except ValueError:
            print("You provided a non-integer character.")