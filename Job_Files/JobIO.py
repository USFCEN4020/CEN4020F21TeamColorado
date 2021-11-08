import pandas as pd
from Job_Files.Job import Job

class JobIO:

    # reads Job objects from file
    # input: string filename = name of file to read from
    # returns: jobList = list of Job objects loaded from file; False if file read error
    def readJobs(self, filename):
        jobList = list()
        try:
            data = pd.read_csv(filename)
            for index, row in data.iterrows():
                job = Job(
                    row["Title"],  
                    row["Description"], 
                    row["Employer"], 
                    row["Location"], 
                    row["Salary"], 
                    row["created_by"])
                jobList.append(job)
            return jobList
        except OSError:
            print("There was a problem reading '" + filename + "'.")
            return False


    # writes list of jobs to file
    # input: jobList = list of Job() objects; string filename = name of file to write to
    # returns: True if write to file successful; False if write to file unsuccessful
    def writeJobs(self, jobList, filename):
        titles = list()
        descriptions = list()
        employers = list()
        locations = list()
        salaries = list()
        creators = list()
        for job in jobList:
            titles.append(job.getTitle())
            descriptions.append(job.getDesc())
            employers.append(job.getEmployer())
            locations.append(job.getLocation())
            salaries.append(job.getSalary())
            creators.append(job.getCreatedBy())

        dictionary = {
            'Title': titles,
            'Description': descriptions,
            'Employer': employers,
            'Location': locations,
            'Salary': salaries,
            'created_by': creators
            }
        
        try:
            data = pd.DataFrame(dictionary)
            data.to_csv(filename, index=False)
            return True
        except OSError:
            print("There was a problem writing to '" + filename + "'.")
            return False