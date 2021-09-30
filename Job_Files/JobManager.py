from Job_Files.Job import Job
from Job_Files.JobIO import JobIO
from User_Files.User import User

class JobManager:


    filename = "Job_Files/jobs.csv"
    jobIO = JobIO()
    jobList = jobIO.readJobs(filename)


    # creates a job listing 
    # returns: job = Job() object that was created; False if jobsList already full
    def createJobListing(self, user):
        # check to see if max amount of jobs posted
        if len(JobManager.jobList) >= 5:
            print("Maximum amount of jobs listings has already been posted. Please come back later!")
            return False
        else:
            # get user input
            print("Please enter the following fields...")
            title = str(input("Job Title: "))
            desc = str(input("Job Description: "))
            employer = str(input("Employer: "))
            location = str(input("Location: "))
            salary = str(input("Salary: "))
            created_by = str(user.getFirstName() + ' ' + user.getLastName())

            # create Job object and append to list
            job = Job(title, desc, employer, location, salary, created_by)
            JobManager.jobList.append(job)
            return job


    # close function to write Job data to file before program terminates
    # NO RETURN VALUE
    def close(self):
        print("Writing to 'jobs.csv'...")
        self.jobIO.writeJobs(self.jobList, self.filename)
        print("Write finished.")
        return

