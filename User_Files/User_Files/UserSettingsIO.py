import pandas as pd
from User_Files.UserSettings import Settings
from User_Files.User import User

class UserSettingsIO:

    # reads user settings from file and assigns them to corresponding user
    # input: userList = list of users from UserManager; string filename = name of file to read
    # returns: settingsList = list containing the settings config for all User objects; False if file read error
    def readUserSettings(self, userList, filename):
        settingsList = list()
        try:
            data = pd.read_csv(filename)
            # loop through userList and load all user's settings
            for user in userList:
                username = user.getUsername()
                for index, row in data.iterrows():
                    # look for setting config that matches user and set user's settings to found settings
                    if username == row["Username"]:
                        settings = Settings(
                            row["Username"], 
                            row["Accept_Privacy_Policy"], 
                            row["email"], 
                            row["sms"],
                            row["ads"],
                            row["language"])
                        user.setSettings(settings)
                        settingsList.append(settings)
            return settingsList
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False


    # updates existing user settings in file
    # input: settingsList = list of Settings objects from UserManager; string filename = name of file to write to
    # returns: True if write to file successful; False if write to file unsuccessful
    def updateUserSettings(self, settingsList, filename):
        try:
            data = pd.read_csv(filename)
            for setting in settingsList:
                username = setting.getUsername()
                # find matching setting config in file to update it
                for index, row in data.iterrows():
                    if username == row["Username"]:
                        data.loc[index, 'Accept_Privacy_Policy'] = setting.getSetting1()
                        data.loc[index, 'email'] = setting.getSetting2()
                        data.loc[index, 'sms'] = setting.getSetting3()
                        data.loc[index, 'ads'] = setting.getSetting4()
                        data.loc[index, 'language'] = setting.getLanguage()
            data.to_csv("userSettings.csv", index=False)
            return True
        except OSError:
            print("There was a problem reading/writing from '" + filename + "'.")
            return False


    def writeUserSettings(self, settingsList, filename):
        usernames = list()
        settings1 = list()
        settings2 = list()
        settings3 = list()
        settings4 = list()
        languages = list()
        for setting in settingsList:
            usernames.append(setting.getUsername())
            settings1.append(setting.getSetting1())
            settings2.append(setting.getSetting2())
            settings3.append(setting.getSetting3())
            settings4.append(setting.getSetting4())
            languages.append(setting.getLanguage())

        dictionary = {
            'Username': usernames,
            'Accept_Privacy_Policy': settings1,
            'email': settings2,
            'sms': settings3,
            'ads': settings4,
            'language': languages
            }

        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False   