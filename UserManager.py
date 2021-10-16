from User_Files.User import User
from User_Files.UserIO import UserIO
from User_Files.UserSettings import Settings
from User_Files.UserSettingsIO import UserSettingsIO
import re

# class to deal with User object functions and store User list
class UserManager:


    filename1 = "User_Files/users.csv"
    filename2 = "User_Files/userSettings.csv"
    userIO = UserIO()
    userSettingsIO = UserSettingsIO()
    userList = userIO.readUsers(filename1)
    userSettingsIO.readUserSettings(userList, filename2)
    settingsList = list()


    # function to get user input and create a new User object
    # returns: newUser = newly created User object; False if the list of user accounts is already full
    def createAccount(self):
        # check to see if userList is at maximum amount of accounts
        if len(self.userList) >= 6:
            print("The maximum amount of accounts has already been made!")
            return False
        # if room for more accounts, get user input and add account to list
        else:
            username = str(input("Provide the username for the new account: "))
            while True:
                password = str(input("Provide password of the new account: "))
                if (len(password) < 8 and len(password) > 12):
                    print("Your password should be between 8 and 12 characters")
                    continue
                elif not re.search("[a-z]", password):
                    print("Your password should have a lower case letter")
                    continue
                elif not re.search("[A-Z]", password):
                    print("Your password should have an upper case letter")
                    continue
                elif not re.search("[0-9]", password):
                    print("Your password should have an integer")
                    continue
                elif not re.search("[!-/]", password):
                    print("Your password should have a special character")
                    continue
                elif re.search("\s", password):
                    print("Your password contains a forbidden character")
                    continue
                else:
                    print("Valid Password")
                    break
            # end while
            firstName = str(input("Provide your first name: "))
            lastName = str(input("Provide your last name: "))

            newUser = User(username, password, firstName, lastName)
            self.userList.append(newUser)
            self.userSettingsIO.writeUserSettings(newUser.getSettings(), self.filename2)
            self.settingsList.append(newUser.getSettings())

            print("Account successfully created. Returning home...\n")
            return newUser

    
    # function to search for an existing InCollege user
    # returns: user = User() object for user being searched for; False if user does not exist or error
    def userSearch(self):
        print("     Search-A-User Page      \n")
        # get user input
        try:
            firstName = str(input("Please enter the FIRST NAME of the user you would like to search for: "))
            lastName = str(input("Please enter the LAST NAME of the user you would like to search for: "))
        except ValueError:
            print("Error getting user input. Try again later.")
            return False

        # loop through list to find user
        for user in self.userList:
            if firstName == user.getFirstName() and lastName == user.getLastName():
                print("This person is a part of the InCollege system.")
                print("Returning to home page...")
                return user

        print("This person is not yet a part of the InCollege system.")
        print("Returning to home page...")
        return False


    # function to log the user in
    # returns: user = User() object from userList that was logged into; False if the function exits in error
    def logIn(self):
        print("     Log-In Page      \n")
        while True:
            try:
                # get username and password input
                try:
                    username = str(input("Username: "))
                    password = str(input("Password: "))
                except ValueError:
                    print("There was an error receiving the username and password. Please try again later.")
                    return False
                
                # loop through userList to check all users
                for user in self.userList:
                    if username == user.getUsername() and password == user.getPassword():
                        print("Login Successful! Returning to home page...")
                        return user
                    else:
                        tryagain = str(input("Incorrect username/password. Would you like to try again? (Y/N):"))
                        if tryagain == 'Y' or tryagain == 'y':
                            continue
                        else:
                            return False
            except TypeError:
                print("There are currently no users loaded in the system.")
                return False


    # function to log out of a user account
    # returns: ALWAYS FALSE
    def logOut(self):
        print("You have successfully been logged out of your account.")
        print("Returning to home page...")
        return False


    # close function to write User data to file before program terminates
    # NO RETURN VALUE
    def close(self):
        # finalize settingsList
        for user in self.userList:
            self.settingsList.append(user.getSettings())
        print("Writing to 'users.csv'...")
        self.userIO.writeUsers(self.userList, self.filename1)
        print("Writing to 'userSettings.csv'...")
        self.userSettingsIO.writeUserSettings(self.settingsList, self.filename2)
        print("Write finished.")
        return