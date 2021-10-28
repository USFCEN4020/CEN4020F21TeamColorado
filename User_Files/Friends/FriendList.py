
class FriendList:
    def __init__(self, username, friend1 = '' ,friend2 = '', friend3 = '',friend4 = '', friend5 = '', friend6 = '', friend7 = '', friend8 = '', friend9 = ''):
        self.username = username
        self.friend1 = friend1
        self.friend2 = friend2
        self.friend3 = friend3
        self.friend4 = friend4
        self.friend5 = friend5
        self.friend6 = friend6
        self.friend7 = friend7
        self.friend8 = friend8
        self.friend9 = friend9

    def getFriendList(self):
        tempList = []
        if(self.friend1 != ''):
            tempList.append(self.friend1)
        if (self.friend2 != ''):
            tempList.append(self.friend2)
        if (self.friend3 != ''):
            tempList.append(self.friend3)
        if (self.friend4 != ''):
            tempList.append(self.friend4)
        if (self.friend5 != ''):
            tempList.append(self.friend5)
        if (self.friend6 != ''):
            tempList.append(self.friend6)
        if (self.friend7 != ''):
            tempList.append(self.friend7)
        if (self.friend8 != ''):
            tempList.append(self.friend8)
        if (self.friend9 != ''):
            tempList.append(self.friend9)
        return tempList

    def setFriendList(self, fUsername):
        if(self.friend1 == ''):
            self.friend1 = fUsername
        elif (self.friend2 != ''):
            self.friend2 = fUsername
        elif (self.friend3 != ''):
            self.friend3 = fUsername
        elif (self.friend4 != ''):
            self.friend4 = fUsername
        elif (self.friend5 != ''):
            self.friend5 = fUsername
        elif (self.friend6 != ''):
            self.friend6 = fUsername
        elif (self.friend7 != ''):
            self.friend7 = fUsername
        elif (self.friend8 != ''):
            self.friend8 = fUsername
        elif (self.friend9 != ''):
            self.friend9 = fUsername