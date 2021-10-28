# Class stores information of user profile

class Profile:
    def __init__(self, username, title = '', major = '', about = '', experience = '', education = ''):
        self.username = username
        self.title = title
        self.major = major
        self.about = about
        self.experience = experience
        self. education = education

    def getUsername(self):
        return self.username

    def setTitle(self, title_input):
        self.title = title_input
    def getTitle(self):
        return self.title

    def setMajor(self, major_input):
        self.major = major_input
    def getMajor(self):
        return self.major

    def setAbout(self, about_input):
        self.about = about_input
    def getAbout(self):
        return self.about

    def setExperience(self, exp_input):
        self.experience = exp_input
    def getExperience(self):
        return self.experience

    def setEducation(self, edu_input):
        self.education = edu_input
    def getEducation(self):
        return self.education
