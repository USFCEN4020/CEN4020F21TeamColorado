import pandas as pd
import ast
import IOHelper
import User_Files.Profiles.UserProfiles
from User_Files.Profiles.UserProfiles import Profile
from User_Files.User import User

class UserProfilesIO:

    # reads user profiles from file and assigns them to corresponding user
    # input: userList = list of users from UserManager; string filename = name of file to read
    # returns: profileList = list containing the profiles for all User objects; False if file read error
    def readUserProfiles(self, userList, filename):
        profileList = list()
        try:
            data = pd.read_csv(filename)
            # loop through userList and load all user's settings
            for user in userList:
                username = user.getUsername()
                for index, row in data.iterrows():
                    # look for setting config that matches user and set user's settings to found settings
                    if username == row["Username"]:
                        profile = Profile(
                            row["Username"], 
                            IOHelper.toBool(row["title"]), 
                            IOHelper.toBool(row["major"]), 
                            IOHelper.toBool(row["university"]),
                            IOHelper.toBool(row["about"]),
                            ast.literal_eval(row["experience"]),    # interprets string as list of lists
                            ast.literal_eval(row["education"]))     # interprets string as list
                        user.setProfile(profile)
                        profileList.append(profile)
            return profileList
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False


    # updates existing user profile in file
    # input: profileList = list of Profile() objects from UserManager; string filename = name of file to write to
    # returns: True if write to file successful; False if write to file unsuccessful
    def updateUserProfiles(self, profileList, filename):
        try:
            data = pd.read_csv(filename)
            for profile in profileList:
                username = profile.getUsername()
                # find matching setting config in file to update it
                for index, row in data.iterrows():
                    if username == row["Username"]:
                        data.loc[index, 'title'] = profile.getTitle()
                        data.loc[index, 'major'] = profile.getMajor()
                        data.loc[index, 'university'] = profile.getUniversity()
                        data.loc[index, 'about'] = profile.getAbout()
                        data.loc[index, 'experience'] = profile.getExperience()
                        data.loc[index, 'education'] = profile.getEducation()
            data.to_csv("userProfiles.csv", index=False)
            return True
        except OSError:
            print("There was a problem reading/writing from '" + filename + "'.")
            return False


    # write profile data to file
    # input: profileList: list of Profile() objects from UserManager; filename = string containing name of file to write to
    # returns: True, if write to file successful; False if unsuccessful
    def writeUserProfiles(self, profileList, filename):
        usernames = list()
        titles = list()
        majors = list()
        universities = list()
        abouts = list()
        experiences = list()
        educations = list()
        for profile in profileList:
            usernames.append(profile.getUsername())
            titles.append(profile.getTitle())
            majors.append(profile.getMajor())
            universities.append(profile.getUniversity())
            abouts.append(profile.getAbout())
            experiences.append(profile.getExperience())
            educations.append(profile.getEducation())

        dictionary = {
            'Username': usernames,
            'title': titles,
            'major': majors,
            'university': universities,
            'about': abouts,
            'experience': experiences,
            'education': educations
            }

        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False   