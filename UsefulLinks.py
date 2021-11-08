import User_Files.User
from Error import Error
from User_Files.User import User
from User_Files.UserManager import UserManager

# display help center message
def helpCenter():
    print("We're here to help!")

# print about us message
def about():
    print("In College: Welcome to In College, the world's largest college student network with many users in many "
          "countries and territories worldwide")

# print press message
def press():
    print("In College Pressroom: Stay on top of the latest news, updates, and reports")

def usefulLinks(loggedIn, userManager):
    e = Error()
    while True:
        print("                         InCollege - Useful Links                          ")
        print("Please select one of the following options to view the associated document.")
        print("""
            1. Sign Up
            2. Help Center
            3. About
            4. Press
            5. Blog
            6. Careers
            7. Developers
            8. Browse InCollege
            9. Business Solutions
            10. Directories
            
            0. Return Home
        """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Sign Up option
            if newOption == 1:
                userManager.createAccount()
            # Help Center option
            elif newOption == 2:
                helpCenter()
            # About option
            elif newOption == 3:
                about()
            # Press option
            elif newOption == 4:
                press()
            # Blog option
            elif newOption == 5:
                e.underConstruction()
            # Careers option
            elif newOption == 6:
                e.underConstruction()
            # Brand Policy option
            elif newOption == 7:
                e.underConstruction()
            # Browse option
            elif newOption == 8:
                e.underConstruction()
            # Business Solutions option
            elif newOption == 9:
                e.underConstruction()
            # Directories Option
            elif newOption == 10:
                e.underConstruction()
            # Return home option
            elif newOption == 0:
                print("Returning to home page...")
                break
        except ValueError:
            print("You provided a non-integer value.")
