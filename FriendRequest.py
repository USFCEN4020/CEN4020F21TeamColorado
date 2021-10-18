import pandas as pd

class FriendRequest:
    def __init__(self, fromUser, toUser):
        self.fromUser = fromUser
        self.toUser = toUser

    def getFrom(self):
        return self.fromUser
    def getTo(self):
        return self.toUser

    def acceptFriend(self, user):
        friends = user.getFriends()
        friends.setFriendList(self.fromUser)
        user.setFriends(friends)