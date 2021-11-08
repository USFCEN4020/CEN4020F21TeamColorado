import pytest
from Notifications import Notification

def testNotificationJobReminder():
    n = Notification()
    assert n.jobReminder() == "Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!"

def testNotificationCreateProfile():
    n = Notification()
    assert n.createProfile() == "Don't forget to create a profile."

def testNotificationNewMessage():
    n = Notification()
    assert n.newMessages() == "You have messages waiting for you."
    
def testNotificationAppCount():
    n = Notification()
    assert n.appCount(3) == "You have applied for 3 jobs."
    assert n.appCount(4) == "You have applied for 4 jobs."
    assert n.appCount(5) == "You have applied for 5 jobs."

def testNotificationNewJob():
    n = Notification()
    assert n.newJob("Software Engineer") == "A new job Software Engineer has been posted."
    assert n.newJob("Software Tester") == "A new job Software Tester has been posted."
    assert n.newJob("Project Lead") == "A new job Project Lead has been posted."
    
def testNotificationJobDelete():
    n = Notification()
    assert n.jobDelete("Software Engineer") == "A job that you applied for has been deleted. Software Engineer is no longer available."
    assert n.jobDelete("Software Tester") == "A job that you applied for has been deleted. Software Tester is no longer available."
    assert n.jobDelete("Project Lead") == "A job that you applied for has been deleted. Project Lead is no longer available."
    
def testNotificationNewUser():
    n = Notification()
    assert n.newUser("John", "Doe") == "John Doe has joined InCollege!"
    assert n.newUser("Elon", "Musk") == "Elon Musk has joined InCollege!"
    assert n.newUser("Jeff", "Bezos") == "Jeff Bezos has joined InCollege!"
