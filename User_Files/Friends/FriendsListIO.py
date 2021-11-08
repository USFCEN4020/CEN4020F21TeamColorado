import pandas as pd
import ast
import User_Files.Friends.FriendsList
from User_Files.Friends.FriendsList import FriendsList
from User_Files.User import User

class FriendsListIO:

    # reads friend lists from file and assigns them to corresponding user
    # input: userList = list of users from UserManager; string filename = name of file to read
    # returns: friendLists = list containing the friend lists for all User objects; False if file read error
    def readFriends(self, userList, filename):
        friendLists = list()
        try:
            data = pd.read_csv(filename)
            # loop through userList and load all user's settings
            for user in userList:
                username = user.getUsername()
                for index, row in data.iterrows():
                    # look for setting config that matches user and set user's settings to found settings
                    if username == row["Username"]:
                        friendList = FriendsList(
                            row["Username"], 
                            ast.literal_eval(row["friends"]),      # interprets string as list
                            ast.literal_eval(row["requests"]))     # interprets string as list
                        user.setFriendsList(friendList)
                        friendLists.append(friendList)
            return friendLists
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False


    # write friend lists to file
    # input: friendLists: list of FriendsList() objects from UserManager; filename = string containing name of file to write to
    # returns: True, if write to file successful; False if unsuccessful
    def writeFriends(self, friendLists, filename):
        usernames = list()
        friends = list()
        requests = list()
        for friendList in friendLists:
            usernames.append(friendList.getUsername())
            friends.append(friendList.getFriends())
            requests.append(friendList.getRequests())

        dictionary = {
            'Username': usernames,
            'friends': friends,
            'requests': requests
            }

        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False