from Job_Files.Job import Job
from Job_Files.JobIO import JobIO
from User_Files.User import User
from csv import writer
class JobManager:


    filename = "Job_Files/jobs.csv"
    filename1 = "Job_Files/appliedJobs.csv"
    jobIO = JobIO()
    jobList = jobIO.readJobs(filename)
    jobApplicationList = jobIO.readJobApplications(filename1)


    # creates a job listing 
    # returns: job = Job() object that was created; False if jobsList already full
    def createJobListing(self, user):
        # check to see if max amount of jobs posted
        if len(JobManager.jobList) >= 10:
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



    def deleteJobListing(self, user):

        if len(JobManager.jobList) <= 1:
            print("Nothing to be deleted")
            return False
        else:
            JobManager.seeJobs(self,user)
            index = int(input("Job's index you want to remove: "))
            JobIO.deleteJobs(self, index-1, "Job_Files/jobs.csv")
            self.jobList = JobIO.readJobs(self,"Job_Files/jobs.csv")
            return True



    def applyForJob(self, user):
        chooseJob = int(input("Please choose the job you would like to apply by index\ne.g. for Job 1 choose 1\n(Type 555, if you would like to see available jobs)\n"))
        # option to see available jobs
        if chooseJob == 555:
            self.seeJobs(user)
        else:
            # to apply
            job = self.jobList[chooseJob - 1]
            if len(self.jobList) >= chooseJob:
                print("You chose ", job.getTitle())
                print("\tDescription: ", job.getDesc())
                print("\tEmployer: ", job.getEmployer())
                print("\tLocation: ", job.getLocation())
                print("\tSalary: ", job.getSalary())
                print("\tCreated by: ", job.getCreatedBy())
                applyOrNot = input("\n\tWould you like to apply for this job?(Y/N)")
                
                if applyOrNot == 'Y':
                    # function to add row to appliedJobs list
                    def append_list_as_row(file_name, list_of_elem):
                        # Open file in append mode
                        with open(file_name, 'a+', newline='') as write_obj:
                            # Create a writer object from csv module
                            csv_writer = writer(write_obj)
                            # Add contents of list as last row in the csv file
                            csv_writer.writerow(list_of_elem)
                    
                    # List of strings
                    applyDetails = [job.getTitle(), user.getUsername()]
                    
                    try:
                        filename = "Job_Files/appliedJobs.csv"
                        # Append a list as new line to appliedJobs csv file
                        append_list_as_row(filename, applyDetails)
                        print("Applied successfully!!\n")
                        return True
                    except OSError:
                        print("There was a problem writing to '" + filename + "'.")
                        return False
                else:
                    print("")
            else:
                print("We don't have a job with that index.\nPlease try again...\n")



    # option to retrieve available jobs
    def seeJobs(self, user):
        print("Number of avaliable jobs: ", len(self.jobList))
        for job in self.jobList:
            print("Job ", (self.jobList.index(job) + 1), '\n')
            print("Title: ", job.getTitle())
            print("Description: ", job.getDesc())
            print("Employer: ", job.getEmployer())
            print("Location: ", job.getLocation())
            print("Salary: ", job.getSalary())
            print("Created by: ", job.getCreatedBy(), '\n')
            return len(self.jobList)



    # option to retrieve applied jobs for specific user
    def seeAppliedJobs(self, user):
        print("Number of applied jobs: ", len(self.jobApplicationList))
        for job in self.jobApplicationList:
            if(job.getApplicant() == user.getUsername()):
                print("Job ", (self.jobApplicationList.index(job) + 1), '\n')
                print("Title: ", job.getTitle())


    # close function to write Job data to file before program terminates
    # NO RETURN VALUE
    def close(self):
        print("Writing to 'jobs.csv'...")
        self.jobIO.writeJobs(self.jobList, self.filename)
        print("Write finished.")
        return

