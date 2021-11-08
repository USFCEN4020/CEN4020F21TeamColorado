class Profile:

    def __init__(self, username, title = False, major = False, university = False, about = False, experience = [ False, False, False ], education = False):
        self.username = username
        self.title = title
        self.major = major
        self.university = university
        self.about = about
        self.experience = experience
        self.education = education


    def getUsername(self):
        return self.username

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setMajor(self, major):
        self.major = major
    def getMajor(self):
        return self.major

    def setUniversity(self, university):
        self.university = university
    def getUniversity(self):
        return self.university

    def setAbout(self, about):
        self.about = about
    def getAbout(self):
        return self.about

    def setExperience(self, experience):
        self.experience = experience
    def getExperience(self):
        return self.experience

    def setEducation(self, education):
        self.education = education
    def getEducation(self):
        return self.education