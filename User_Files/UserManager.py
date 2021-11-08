import User_Files.Settings.UserSettings
import User_Files.Friends.FriendsList
import User_Files.Profiles.UserProfiles
from User_Files.User import User
from User_Files.UserIO import UserIO
from User_Files.Settings.UserSettings import Setting
from User_Files.Profiles.UserProfiles import Profile
from User_Files.Settings.UserSettingsIO import UserSettingsIO
from User_Files.Profiles.UserProfilesIO import UserProfilesIO
from User_Files.Friends.FriendsListIO import FriendsListIO
import re

# class to deal with User object functions and store User list
class UserManager:

    ############################################
    ###  FILENAME 1: Data for Users          ###
    ###  FILENAME 2: Data for User Settings  ###
    ###  FILENAME 3: Data for User Profiles  ###
    ###  FILENAME 4: Data for User Friends   ###
    ############################################
    userFile = "User_Files/users.csv"
    settingsFile = "User_Files/Settings/userSettings.csv"
    profileFile = "User_Files/Profiles/userProfiles.csv"
    friendsFile = "User_Files/Friends/friendLists.csv"

    userIO = UserIO()
    userSettingsIO = UserSettingsIO()
    userProfilesIO = UserProfilesIO()
    friendsListIO = FriendsListIO()
    userList = userIO.readUsers(userFile)

    # read data from file and assign to matching User object
    userSettingsIO.readUserSettings(userList, settingsFile)
    userProfilesIO.readUserProfiles(userList, profileFile)
    friendsListIO.readFriends(userList, friendsFile)

    # lists for writing data on file close
    # note: DO NOT APPEND NEW ITEMS TO THESE LISTS
    # Instead, assign item to corresponding User object and append User() to userList
    # Let close() function loop through userList and append the items to these lists
    settingsList = list()
    profileList = list()
    friendLists = list()


    # function to get user input and create a new User object
    # returns: newUser = newly created User object; False if the list of user accounts is already full
    def createAccount(self):
        # CURRENT MAXIMUM ACCOUNT LIMIT: 10
        if len(self.userList) >= 10:
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


    # search for users in the system by last name
    # input: lastName = string of name to be searched for
    # returns: foundUsers = list of User() objects with the specified last name; False if no users found
    def findUsersByName(self, lastName):
        foundUsers = list()
        for user in self.userList:
            if user.getLastName() == lastName:
                foundUsers.append(user)

        if foundUsers:
            return foundUsers
        else:
            return False


    # search for users in the system by university they attend
    # input: university = string of university to be searched for
    # returns: foundUsers = list of User() objects with the specified university; False if no users found
    def findUsersByUni(self, university):
        foundUsers = list()
        for user in self.userList:
            if user.getProfile().getUniversity() == university:
                foundUsers.append(user)

        if foundUsers:
            return foundUsers
        else:
            return False


    # search for users in the system by their major
    # input: major = string of major to be searched for
    # returns: foundUsers = list of User() objects with the specified university; False if no users found
    def findUsersByMajor(self, major):
        foundUsers = list()
        for user in self.userList:
            if user.getProfile().getMajor() == major:
                foundUsers.append(user)

        if foundUsers:
            return foundUsers
        else:
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
                        print("Incorrect username/password. Please try again.")
                        continue
            except TypeError:
                print("There are currently no users loaded in the system.")
                return False


    # function to log out of a user account
    # returns: ALWAYS FALSE
    def logOut(self):
        print("You have successfully been logged out of your account.")
        print("Returning to home page...")
        return False


    # displays a given profile
    # input: profile = Profile() object to display
    # returns: NO RETURN VALUE
    def displayProfile(self, profile):
        print("""
            Title:      """ + str(profile.getTitle()) + """
            Major:      """ + str(profile.getMajor()) + """
            University: """ + str(profile.getUniversity()) + """
            About:      """ + str(profile.getAbout()) + """
            Experience: A) """ + str(profile.getExperience()[0]) + """
                        B) """ + str(profile.getExperience()[1]) + """
                        C) """ + str(profile.getExperience()[2]) + """
            Education:  """ + str(profile.getEducation()) + """
            """)
        return


    # close function to write User data to file before program terminates
    # NO RETURN VALUE
    def close(self):
        # add all User-field objects to empty lists
        for user in self.userList:
            self.settingsList.append(user.getSettings())
            self.profileList.append(user.getProfile())
            self.friendLists.append(user.getFriendsList())
        print("Writing to '" + self.userFile + "'...")
        self.userIO.writeUsers(self.userList, self.userFile)
        print("Writing to '" + self.settingsFile + "'...")
        self.userSettingsIO.writeUserSettings(self.settingsList, self.settingsFile)
        print("Writing to '" + self.profileFile + "'...")
        self.userProfilesIO.writeUserProfiles(self.profileList, self.profileFile)
        print("Writing to '" + self.friendsFile + "'...")
        self.friendsListIO.writeFriends(self.friendLists, self.friendsFile)
        print("Write finished.")
        return