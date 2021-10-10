import pandas as pd

def profileMenu(loggedIn):
    while True:
        title = loggedIn.getProfile().getTitle()
        major = loggedIn.getProfile().getMajor()
        about = loggedIn.getProfile().getAbout()
        experience = loggedIn.getProfile().getExperience()
        education = loggedIn.getProfile().getEducation()
        print("                       InCollege - Profile Menu                            ")
        print("Please select one of the following options to view the associated parts   .")
        print("""
                    1. View Title
                    2. View Major
                    3. View About
                    4. View Experience
                    5. View Education

                    6. Edit Profile

                    0. Return Home
                """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Show Title
            if newOption == 1:
                print(title)
            # Show Major
            elif newOption == 2:
                print(major)
            # Show About
            elif newOption == 3:
                print(about)
            # Show Experience
            elif newOption == 4:
                print(experience)
            # Show Education
            elif newOption == 5:
                print(education)
            # Edit Profile
            elif newOption == 6:
                editProfile(loggedIn)

            # Return Home
            elif newOption == 0:
                print("Returning to home page...")
                break

        except ValueError:
            print("You provided a non-integer value.")

def editProfile(loggedIn):
    while True:
        print("                       InCollege - Edit Profile                            ")
        print("Please select one of the following options to view the associated parts   .")
        print("""
                                1. Edit Title
                                2. Edit Major
                                3. Edit About
                                4. Edit Experience
                                5. Edit Education

                                0. Return to Menus
                            """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Edit Title
            if newOption == 1:
                title = input("Please enter new Title: ")
                loggedIn.getProfile().setTitle(title)
            # Edit Major
            elif newOption == 2:
                major = input("Please enter new Major: ")
                loggedIn.getProfile().setMajor(major)
            # Edit About
            elif newOption == 3:
                about = input("Please enter new About: ")
                loggedIn.getProfile().setAbout(about)
            # Edit Experience
            elif newOption == 4:
                experience = input("Please enter new Experience: ")
                loggedIn.getProfile().setExperience(experience)
            # Edit Education
            elif newOption == 5:
                education = input("Please enter new Education: ")
                loggedIn.getProfile().setEducation(education)
            # Return to ProfileMenus
            elif newOption == 0:
                print("Returning to profiles page...")
                break
        except ValueError:
            print("You provided a non-integer value.")