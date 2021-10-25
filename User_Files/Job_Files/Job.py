# class for creating a Job object
class Job:

    def __init__(self, title, desc, employer, location, salary, created_by):
        self.title = title
        self.desc = desc
        self.employer = employer
        self.location = location
        self.salary = salary
        self.created_by = created_by

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setDesc(self, desc):
        self.desc = desc
    def getDesc(self):
        return self.desc

    def setEmployer(self, employer):
        self.employer = employer
    def getEmployer(self):
        return self.employer

    def setLocation(self, location):
        self.location = location
    def getLocation(self):
        return self.location

    def setSalary(self, salary):
        self.salary = salary
    def getSalary(self):
        return self.salary

    def setCreatedBy(self, created_by):
        self.created_by = created_by
    def getCreatedBy(self):
        return self.created_by