import pandas as pd
from FriendRequest import FriendRequest

class FriendRequestIO:
    def readFriendRequests(self, userList, filename):
        friendRequests = list()
        try:
            data = pd.read_csv(filename)
            # loop through userList and load all user's settings
            for user in userList:
                username = user.getUsername()
                for index, row in data.iterrows():
                    # look for setting config that matches user and set user's settings to found settings
                    if username == row["To"]:
                        request = FriendRequest(
                            row["To"],
                            row["From"])
                        friendRequests.append(request)
            return friendRequests
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False