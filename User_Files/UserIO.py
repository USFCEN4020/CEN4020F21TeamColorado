import pandas as pd
from User_Files.User import User

# class for reading and writing User objects to/from a file
class UserIO:

    # reads users from files and creates list of user objects
    # input: string filename = name of file to read
    # returns: list userList = list of all users from 'users.csv'; False if an error occurs
    def readUsers(self, filename):
        userList = []
        try:
            data = pd.read_csv(filename)
            for index, row in data.iterrows():
                user = User(row["Username"], row["Password"], row["First_Name"], row["Last_Name"], row["Status"])
                userList.append(user)
            return userList
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False

    # writes users to file
    # input: userList = final list of users immediately before the program terminates; string filename = name of file to write to
    # returns: True if write to file was successful; False if write to file was unsuccessful
    def writeUsers(self, userList, filename):
        usernames = list()
        passwords = list()
        firstNames = list()
        lastNames = list()
        memberships = list()
        for user in userList:
            usernames.append(user.getUsername())
            passwords.append(user.getPassword())
            firstNames.append(user.getFirstName())
            lastNames.append(user.getLastName())
            memberships.append(user.getStatus())

        dictionary = {
            'Username': usernames,
            'Password': passwords,
            'First_Name': firstNames,
            'Last_Name': lastNames,
            'Status': memberships 
            }
        
        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False
