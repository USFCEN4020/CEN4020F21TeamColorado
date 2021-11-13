import Error
from User_Files.User import User
from User_Files.UserManager import UserManager

takenCourses = [False, False, False, False, False]
userManager = UserManager()

# main menu for training
def trainingMenu(loggedIn, ):
    while True:
        print("                Training")
        print("Please select one of the following options")
        print("""
            1. Training and Education
            2. IT Help Desk
            3. Business Analysis and Strategy
            4. Security
            
            0. Back to home page
            """)
        try:
            e = Error()
            newOption = int(input("Choice: "))
            print("\n")
            if newOption == 1:
                e.underConstruction()
            elif newOption == 2:
                print("Coming Soon!")
            elif newOption == 3:
                if not loggedIn:
                    while True:
                        print("     Business Analysis and Strategy")
                        print("Please select one of the following options")
                        print("""
                            1. How to use In College learning
                            2. Train the Trainer
                            3. Gamification of learning

                            0. Back to training page

                            Not seeing what you’re looking for? Sign in to see all 7,609 results.
                            """)
                        try:
                            e = Error()
                            newOption = int(input("Choice: "))
                            print("\n")
                            if newOption == 1:
                                loggedIn = userManager.createAccount()
                            elif newOption == 2:
                                loggedIn = userManager.createAccount()
                            elif newOption == 3:
                                loggedIn = userManager.createAccount()
                            elif newOption == 0:
                                print("Returning to previous page...")
                                break
                        except ValueError:
                            print("A Non-integer was provided.")
                else:
                    while True:
                        print("     Business Analysis and Strategy")
                        print("Please select one of the following options")
                        print("""
                                               1. How to use In College learning
                                               2. Train the Trainer
                                               3. Gamification of learning
                                               4. Understanding the Architectural Design Process
                                               5. Project Management Simplified

                                               0. Back to training page

                                               Not seeing what you’re looking for? Sign in to see all 7,609 results.
                                               """)
                        try:
                            e = Error()
                            newOption = int(input("Choice: "))
                            print("\n")
                            if newOption == 1 and takenCourses[1] == False:
                                print("You have now completed this training.")
                                takenCourses[1] = True;
                            elif newOption == 1 and takenCourses[1] == True:
                                temp = input("""You have already taken this course, do you want to take it again?
                                             (Y/N): """)
                                if temp == "Y":
                                    print("You have now completed this training.")
                                else:
                                    print("Course Cancelled")
                            elif newOption == 2 and takenCourses[2] == False:
                                print("You have now completed this training.")
                                takenCourses[2] = True;
                            elif newOption == 2 and takenCourses[2] == True:
                                temp = input("""You have already taken this course, do you want to take it again?
                                             (Y/N): """)
                                if temp == "Y":
                                    print("You have now completed this training.")
                                else:
                                    print("Course Cancelled")
                            elif newOption == 3 and takenCourses[3] == False:
                                print("You have now completed this training.")
                                takenCourses[3] = True;
                            elif newOption == 3 and takenCourses[3] == True:
                                temp = input("""You have already taken this course, do you want to take it again?
                                             (Y/N): """)
                                if temp == "Y":
                                    print("You have now completed this training.")
                                else:
                                    print("Course Cancelled")
                            elif newOption == 4 and takenCourses[4] == False:
                                print("You have now completed this training.")
                                takenCourses[4] = True;
                            elif newOption == 4 and takenCourses[4] == True:
                                temp = input("""You have already taken this course, do you want to take it again?
                                             (Y/N): """)
                                if temp == "Y":
                                    print("You have now completed this training.")
                                else:
                                    print("Course Cancelled")
                            elif newOption == 5 and takenCourses[5] == False:
                                print("You have now completed this training.")
                                takenCourses[5] = True;
                            elif newOption == 5 and takenCourses[5] == True:
                                temp = input("""You have already taken this course, do you want to take it again?
                                             (Y/N): """)
                                if temp == "Y":
                                    print("You have now completed this training.")
                                else:
                                    print("Course Cancelled")
                            elif newOption == 0:
                                print("Returning to previous page...")
                                break
                        except ValueError:
                            print("A Non-integer was provided.")


            elif newOption == 4:
                print("Coming Soon!")
            elif newOption == 0:
                print("Returning back to home page...")
                break
        except ValueError:
            print("A Non-integer was provided.")

def businessAnS():
    while True:
        print("     Business Analysis and Strategy")
        print("Please select one of the following options")
        print("""
            1. How to use In College learning
            2. Train the Trainer
            3. Gamification of learning

            0. Back to training page
            
            Not seeing what you’re looking for? Sign in to see all 7,609 results.
            """)
        try:
            e = Error()
            newOption = int(input("Choice: "))
            print("\n")
            if newOption == 1:
                e.underConstruction()
            elif newOption == 2:
                print("Coming Soon!")
            elif newOption == 3:
                print()
            elif newOption == 0:
                print("Returning to previous page...")
                break
        except ValueError:
            print("A Non-integer was provided.")
