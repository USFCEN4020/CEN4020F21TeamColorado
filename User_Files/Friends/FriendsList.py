class FriendsList:

    def __init__(self, username, friends = [], requests = []):
        self.username = username
        self.friends = friends
        self.requests = requests

    
    def getUsername(self):
        return self.username

    def setFriends(self, friends):
        self.friends = friends
    def getFriends(self):
        return self.friends

    def setRequests(self, requests):
        self.requests = requests
    def getRequests(self):
        return self.requests