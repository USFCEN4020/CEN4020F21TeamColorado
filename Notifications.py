# Error file for team Colorado
# Implemented via python
class Notification:
    def __init__(self):
        print("Notifications...")

    def jobReminder(self):
        print("Remember - you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")
    
    def createProfile(self):
        print("Don't forget to create a profile.")
    
    def newMessages(self):
        print("You have messages waiting for you.")
    
    def appCount(self, x):
        print("You have applied for %d jobs." % (x))
    
    def newJob(self, title):
        print("A new job ", title, "has been posted.")
    
    def jobDelete(self, title):
        print("A job that you applied for has been deleted. ", title, " is no longer available.")
    
    def newUser(self, firstName, lastName):
        print(firstName, " ", lastName, " has joined InCollege!")