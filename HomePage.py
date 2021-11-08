# Home page file for team Colorado
# Implemented via python
import User_Files
import User_Files.Settings.UserSettings
import User_Files.Friends.FriendHandler
import ImportantLinks
import UsefulLinks
import ProfilePage
import FriendsPage
import SkillsPage
import JobsPage
import re
from Error import Error
from User_Files.User import User
from User_Files.UserManager import UserManager
from User_Files.Settings.UserSettings import Setting
from Job_Files.Job import Job
from Job_Files.JobManager import JobManager
from User_Files.Friends.FriendHandler import FriendHandler

# empy boolean representing no logged in user
# when logged in, value will be the logged-in User() object
loggedIn = False

# manager objects to perform object operations
userManager = UserManager()
jobManager = JobManager()
friendHandler = FriendHandler()

# main() loop
while True:

    # home page for user who is not logged in
    if not loggedIn:
        print("\n              Home Page               ")
        print("Please select one of the following options.")
        print("""
            1. Log-In
            2. Create an account
            3. Search for a job
            4. Find someone you know
            5. Learn a new skill

            6. Useful Links
            7. InCollege Important Links

            Student success story:
            My name is John Shephard and I graduated from college with a BCS degree. I stumbled
            upon InCollege when searching for jobs before graduating. Using this program, I
            was instantly connected with hundreds of employers who all met or exceeded my desired
            criteria. I now have been working with a company for 4 years and have already
            recieved multiple promotions! Thanks InCollege!\n
            8. Watch a video to see more of my story

            0. Exit
        """)
    # home page for logged in user
    else:
        # get notification for pending friend requests
        requestsMsg = friendHandler.friendNotif(loggedIn)
        if not requestsMsg:
            requestsMsg = ''

        print("\n              Home Page               ")
        print("Please select one of the following options")
        print("""
            1. View profile/Log-out (logged in as """ + loggedIn.getFirstName() + ' ' + loggedIn.getLastName() + """)
            2. Create an account
            3. Search for a job
            4. Find or view friends """ + str(requestsMsg) + """
            5. Learn a new skill

            6. Useful Links
            7. InCollege Important Links

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
            loggedIn = ProfilePage.profileMenu(loggedIn, userManager)
        elif newOption == 1 and not loggedIn:
            # Call the log-out user function
            loggedIn = userManager.logIn()


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
        elif newOption == 4 and not loggedIn:
            # call the user search user function
            userManager.userSearch()
        elif newOption == 4 and loggedIn:
            # open up the friends page
            FriendsPage.friendsMenu(loggedIn, userManager)


        ###################################################
        ###     OPTION 5: Learn a new skill option      ###
        ###################################################
        elif newOption == 5:
            # Call the SkillsPage.py main menu function
            SkillsPage.skillsMenu()


        #############################################
        ###     OPTION 6: Useful Links option     ###
        #############################################
        elif newOption == 6:
            UsefulLinks.usefulLinks(loggedIn, userManager)


        ##########################################################
        ###     OPTION 7: InCollege Important Links option     ###
        ##########################################################
        elif newOption == 7:
            ImportantLinks.importantLinksMenu(loggedIn)


        #############################################
        ###     OPTION 8: Play video option       ###
        #############################################
        elif newOption == 8 and loggedIn:
            print("Video is now playing.")


        ##############################################
        ###     OPTION 0: Exit program option      ###
        ##############################################
        elif newOption == 0:
            # exit program
            try:
                userManager.close()
                jobManager.close()
            except OSError:
                print("Error writing to file on program close. Forcibly exiting program...")
                exit()
            print("Program closing.")
            exit()


    # input error handler
    except ValueError:
        print("You provided a non-integer character.")