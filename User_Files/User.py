from User_Files.Settings import UserSettings
from User_Files.Profiles import UserProfiles
from User_Files.Friends import FriendsList
from User_Files.Settings.UserSettings import Setting
from User_Files.Profiles.UserProfiles import Profile
from User_Files.Friends.FriendsList import FriendsList

# class for creating a User object
class User:

    def __init__(self, username, password, firstName, lastName):
        self.username = username
        self.password = password
        self.firstName = firstName
        self.lastName = lastName
        self.settings = Setting(username)
        self.profile = Profile(username)
        self.friendsList = FriendsList(username)

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

    def setFriendsList(self, friendsList):
        self.friendsList = friendsList
    def getFriendsList(self):
        return self.friendsList