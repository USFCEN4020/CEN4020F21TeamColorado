import Error
from User_Files.User import User
from Job_Files.Job import Job
import Job_Files.JobManager

# main function
# input: loggedIn = string containing logged-in user's name, or False if empty (nobody logged in)
def jobMenu(loggedIn, jobManager):

    while True:
        if jobManager.noteJobDeleted(loggedIn):
            print("")
        else:
            print("Notification - Applied job was deleted\n")

        print("             Job Board             ")
        print("Please select one of the following options")
        print("""
        1. Find a job listing
        2. Create a job listing (must be logged in)
        3. Apply for a job (must be logged in)
        4. See applied jobs (must be logged in)
        5. Delete job by title
        6. Return
        """)
        try:

            newOption = int(input("Choice: "))
            print('\n')
            # Find a job listing option
            if newOption == 1:
                jobManager.seeJobs(loggedIn)
            # Create a job listing option
            elif newOption == 2 and loggedIn:
                jobManager.createJobListing(loggedIn)
            # Deny job creation if not logged in
            elif newOption == 2 and not loggedIn:
                print("You must be logged in to post a job listing!\n")
            # Job application option
            elif newOption == 3 and loggedIn:
                jobManager.applyForJob(loggedIn)
            # Deny job creation if not logged in
            elif newOption == 3 and not loggedIn:
                print("You must be logged in to apply for a job!\n")
            # See applied jobs option
            elif newOption == 4 and loggedIn:
                jobManager.seeAppliedJobs(loggedIn)
            # Deny job creation if not logged in
            elif newOption == 4 and not loggedIn:
                print("You must be logged in to see your applied jobs!\n")
            # Go back to home page option
            elif newOption == 5 and loggedIn:
                jobManager.deleteJobListing(loggedIn)
            elif newOption == 5 and not loggedIn:
                print("You must be logged in to see your applied jobs!\n")
            elif newOption == 6:
                print("Returning...")
                break
        except ValueError:
            print("You provided a non-integer character.")