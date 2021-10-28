# Home page file for team Colorado
# Implemented via python
from Error import Error
from User_Files.UserSettings import Settings
from User_Files.User import User
from User_Files.UserManager import UserManager
from Job_Files.Job import Job
from Job_Files.JobManager import JobManager
import ImportantLinks
import UsefulLinks
import SkillsPage
import JobsPage
import ProfileMenu
from FriendRequestIO import FriendRequestIO
import FriendRequest
import re

# empy boolean representing no logged in user
# when logged in, value will be the logged-in User() object
loggedIn = False

# manager objects to perform object operations
userManager = UserManager()
jobManager = JobManager()

for setting in userManager.settingsList:
    print(setting.getUsername())

# main() loop
while True:

    # block of code for user who is not logged in
    if not loggedIn:
        print("\n              Home Page               ")
        print("Please select one of the following options")
        print("""
            1. Log-In
            2. Create an account
            3. Search for a job
            4. Find someone you know
            5. Learn a new skill
            6. View profile

            7. Useful Links
            8. InCollege Important Links

            0. Exit

            Student success story:
            My name is John Shephard and I graduated from college with a BCS degree. I stumbled
            upon InCollege when searching for jobs before graduating. Using this program, I
            was instantly connected with hundreds of employers who all met or exceeded my desired
            criteria. I now have been working with a company for 4 years and have already
            recieved multiple promotions! Thanks InCollege!\n
            9. Watch a video to see more of my story
        """)
    else:
        print("\n              Home Page               ")
        print("Please select one of the following options")
        print("""
            1. Log-Out (logged in as """ + loggedIn.getFirstName() + ' ' + loggedIn.getLastName() + """)
            2. Create an account
            3. Search for a job
            4. Find someone you know
            5. Learn a new skill
            6. View your profile

            7. Useful Links
            8. InCollege Important Links

            0. Exit
        """)
    try:
        newOption = int(input("Choice: "))
        print()


        #######################################
        ###     OPTION 1: Log-In option     ###
        #######################################
        if newOption == 1 and loggedIn:
            # Call the Log-In user function
            loggedIn = userManager.logOut()
        elif newOption == 1 and not loggedIn:
            # Call the log-out user function
            loggedIn = userManager.logIn()
            try:
                frIO = FriendRequestIO()
                frRequests = list()
                frRequests = frIO.readFriendRequests(loggedIn.getUsername(), "friendRequests.csv")
                if(len(frRequests) > 0):
                    request = frRequests.pop()
                    print("You have friend request from " + request.getFrom() + ".")
                    accept = input("Accept?(y/n): ")
                    if (accept == 'y'):
                        request.acceptFriend(loggedIn)
            except:
                print("(⚠️ Exception occurred when loading friend requests...)")



        ###################################################
        ###     OPTION 2: Create an account option      ###
        ###################################################
        elif newOption == 2:
            # Call the create account user function
            userManager.createAccount()


        #################################################
        ###     OPTION 3: Search for a job option     ###
        #################################################
        elif newOption == 3:
            # Call the JobsPage.py menu function
            JobsPage.jobMenu(loggedIn, jobManager)            


        #######################################################
        ###     OPTION 4: Find someone you know option      ###
        #######################################################
        elif newOption == 4:
            # call the user search user function
            userManager.userSearch()


        ###################################################
        ###     OPTION 5: Learn a new skill option      ###
        ###################################################
        elif newOption == 5:
            # Call the SkillsPage.py main menu function
            SkillsPage.skillsMenu()

        #############################################
        ###     OPTION 6: Profile                 ###
        #############################################
        elif newOption == 6 and not loggedIn:
            print("Have to be logged in to view profile")
        elif newOption == 6 and loggedIn:
            ProfileMenu.profileMenu(loggedIn)



        #############################################
        ###     OPTION 7: Useful Links option     ###
        #############################################
        elif newOption == 7:
            UsefulLinks.usefulLinks(loggedIn)


        ##########################################################
        ###     OPTION 8: InCollege Important Links option     ###
        ##########################################################
        elif newOption == 8:
            ImportantLinks.importantLinksMenu(loggedIn)

        ##############################################
        ###     OPTION 0: Exit program option      ###
        ##############################################
        elif newOption == 0:
            # exit program
            userManager.close()
            jobManager.close()
            print("Program closing.")
            exit()


        #############################################
        ###     OPTION 9: Play video option       ###
        #############################################
        elif newOption == 9 and loggedIn:
            print("Video is now playing.")


    # input error handler
    except ValueError:
        print("You provided a non-integer character.")
