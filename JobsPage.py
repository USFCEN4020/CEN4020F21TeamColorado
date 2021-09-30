import Error
from User_Files.User import User
from Job_Files.Job import Job
import Job_Files.JobManager

# main function
# input: loggedIn = string containing logged-in user's name, or False if empty (nobody logged in)
def jobMenu(loggedIn, jobManager):
    while True:
        print("             Job Board             ")
        print("Please select one of the following options")
        print("""
        1. Find a job listing
        2. Create a job listing (must be logged in)
        
        3. Back to home page
        """)
        try:
            newOption = int(input("Choice: "))
            print('\n')
            # Find a job listing option
            if newOption == 1:
                Error.underConstruction()
            # Create a job listing option
            elif newOption == 2 and loggedIn:
                jobManager.createJobListing(loggedIn)
            # Deny job creation if not logged in
            elif newOption == 2 and not loggedIn:
                print("You must be logged in to post a job listing!\n")
            # Back to home page option
            elif newOption == 3:
                print("Returning to home page...")
                break
        except ValueError:
            print("You provided a non-integer character.")