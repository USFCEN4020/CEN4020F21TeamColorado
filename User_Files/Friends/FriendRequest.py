class FriendRequest:

    def __init__(self, sender, recipient):
        self.sender = sender
        self.recipient = recipient

    def setSender(self, sender):
        self.sender = sender
    def getSender(self):
        return self.sender

    def setRecipient(self, recipient):
        self.recipient = recipient
    def getRecipient(self):
        return self.recipient