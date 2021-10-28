# class to store settings for a User object
# setting 1 = Accepted Privacy Policy [True/False]
# setting 2 = Recieve promotion emails [True/False]
# setting 3 = Recieve promotion SMS [True/False]
# setting 4 = Recieve advertisements [True/False]
# language = Currently only English and Spanish ["EN"/"ES"]
class Settings:

    def __init__(self, username, setting1 = False, setting2 = True, setting3 = True, setting4 = True, language = "EN"):
        self.username = username
        self.setting1 = setting1
        self.setting2 = setting2
        self.setting3 = setting3
        self.setting4 = setting4
        self.language = language

    def getUsername(self):
        return self.username

    def setSetting1(self, setting1):
        self.setting1 = setting1
    def getSetting1(self):
        return self.setting1

    def setSetting2(self, setting2):
        self.setting2 = setting2
    def getSetting2(self):
        return self.setting2

    def setSetting3(self, setting3):
        self.setting3 = setting3
    def getSetting3(self):
        return self.setting3

    def setSetting4(self, setting4):
        self.setting4 = setting4
    def getSetting4(self):
        return self.setting4

    def setLanguage(self, language):
        self.language = language
    def getLanguage(self):
        return self.language
