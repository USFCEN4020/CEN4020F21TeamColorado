import pytest
from testFileCore import set_keyboard_input, get_display_output, makeMultiInput

# Tested IOs
from Job_Files.JobIO import JobIO
from Job_Files.Job import Job

from User_Files.UserIO import UserIO
from User_Files.User import User

from User_Files.Settings.UserSettingsIO import UserSettingsIO
from User_Files.Settings.UserSettings import Settings

# Tests for JobIO
def test_readJobs():

    assert JobIO.readJobs('Job_Files/jobs.csv') != False

def test_writeJobs():
    testJobList = list()
    tester1 = Job('Tester1', 'Test Case Dummy 1', 'Nobody', 'Nowhere', '$00.00 per year', 'Andrey K.')
    tester2 = Job('Tester2', 'Test Case Dummy 2', 'Nobody', 'Nowhere', '$00.00 per year', 'Andrey K.')
    testJobList.append(tester1)
    testJobList.append(tester2)
    assert JobIO.writeJobs(testJobList, 'PyTest/testjobs.csv') != False

def test_deleteJobs():

    assert JobIO.deleteJobs(1, 'PyTest/testjobs.csv') != False

def test_readApplications():

    assert JobIO.readJobApplications('Job_Files/appliedJobs.csv') != False

# Tests for the UserIO
def test_readUser():

    assert UserIO.readUsers('User_Files/users.csv') != False

def test_writeUsers():
    userList = list()
    user1 = User('Tester1', 'Password#123', 'John', 'Smith', 'Standard')
    user2 = User('Tester2', 'Password#123', 'Mary', 'Smith', 'Standard')
    userList.append(user1)
    userList.append(user2)
    assert UserIO.writeUsers(userList, 'PyTests/testusers.csv') != False

# Tests for UserSettingsIO
def test_readUserSettings():
    userList = UserIO.readUsers('User_Files/users.csv')

    assert UserSettingsIO.readUserSettings(userList, 'PyTest/testuserSettings.csv') != False

def test_updateSettings():
    settingsList= list()
    changedAdminSettings = Settings('Admin', False, False, False, False, "EN")
    Tester1Settings = Settings('Tester1', True, True, True, True, "EN")
    settingsList.append(changedAdminSettings)
    settingsList.append(Tester1Settings)
    assert UserSettingsIO.updateUserSettings(settingsList, 'PyTests/testuserSettings.csv') != False

def test_writeSettings():
    settingsList = list()
    Tester2Setting = Settings('Tester2')
    settingsList.append(Tester2Setting)
    assert UserSettingsIO.writeUserSettings(settingsList, 'PyTests/testuserSettings.csv') != False