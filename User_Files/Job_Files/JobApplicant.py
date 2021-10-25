# class for creating a Job object
class JobApplicant:

    def __init__(self, title, applicant):
        self.title = title
        self.applicant = applicant

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setApplicant(self, desc):
        self.applicant = applicant
    def getApplicant(self):
        return self.applicant