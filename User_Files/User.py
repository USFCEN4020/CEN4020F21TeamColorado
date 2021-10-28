from User_Files.UserSettings import Settings
from User_Files.UserProfiles import Profile
from User_Files.UserFriends import Friends

# class for creating a User object
class User:

    def __init__(self, username, password, firstName, lastName, status):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.status = status
        self.settings = Settings(username)
        self.profile = Profile(username)
        self.friends = Friends(username)

    inbox = []      # List to hold inbox messages

    def setUsername(self, username):
        self.username = username
    def getUsername(self):
        return self.username

    def setPassword(self, password):
        self.password = password
    def getPassword(self):
        return self.password

    def setFirstName(self, firstName):
        self.firstName = firstName
    def getFirstName(self):
        return self.firstName

    def setLastName(self, lastName):
        self.lastName = lastName
    def getLastName(self):
        return self.lastName

    def setSettings(self, settings):
        self.settings = settings
    def getSettings(self):
        return self.settings

    def setProfile(self, profile):
        self.profile = profile
    def getProfile(self):
        return self.profile

    def setFriends(self, friends):
        self.friends = friends
    def getFriends(self):
        return self.friends

    def setStatus(self, status):
        self.status = status
    def getStatus(self):
        return self.status