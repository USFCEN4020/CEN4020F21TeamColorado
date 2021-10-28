import pandas as pd
from UserProfiles import Profile
from User_Files.User import User

class UserProfilesIO:

    # reads user settings from file and assigns them to corresponding user
    # input: userList = list of users from UserManager; string filename = name of file to read
    # returns: profileList = list containing the profile details for all User objects; False if file read error
    def readUserProfile(self, userList, filename):
        profileList = list()
        try:
            data = pd.read_csv(filename)
            # loop through userList and load all user's profile
            for user in userList:
                username = user.getUsername()
                for index, row in data.iterrows():
                    # look for setting config that matches user and set user's settings to found settings
                    if username == row["Username"]:
                        profiles = Profile(
                            row["Username"],
                            row["Title"],
                            row["Major"],
                            row["About"],
                            row["Experience"],
                            row["Education"])
                        user.setProfile(profiles)
                        profileList.append(profiles)
            return profileList
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False


    # updates existing user profiles in file
    # input: profileList = list of Profile objects from UserManager; string filename = name of file to write to
    # returns: True if write to file successful; False if write to file unsuccessful
    def updateUserProfile(self, profileList, filename):
        try:
            data = pd.read_csv(filename)
            for profile in profileList:
                username = profile.getUsername()
                # find matching setting config in file to update it
                for index, row in data.iterrows():
                    if username == row["Username"]:
                        data.loc[index, 'Title'] = profile.getTitle()
                        data.loc[index, 'Major'] = profile.getMajor()
                        data.loc[index, 'About'] = profile.getAbout()
                        data.loc[index, 'Experience'] = profile.getExperience()
                        data.loc[index, 'Education'] = profile.getEducation()
            data.to_csv("userProfiles.csv", index=False)
            return True
        except OSError:
            print("There was a problem reading/writing from '" + filename + "'.")
            return False


    def writeUserProfiles(self, profileList, filename):
        usernames = list()
        titles = list()
        major = list()
        about = list()
        experience = list()
        education = list()
        for profile in profileList:
            usernames.append(profile.getUsername())
            titles.append(profile.getTitle())
            major.append(profile.getMajor())
            about.append(profile.getAbout())
            experience.append(profile.getExperience())
            education.append(profile.getEducation())

        dictionary = {
            'Username': usernames,
            'Title': titles,
            'Major': major,
            'About': about,
            'Experience': experience,
            'Education': education
            }

        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False