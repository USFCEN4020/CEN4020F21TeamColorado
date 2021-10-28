from User_Files import User

# This class is used to create and send a text message from one user to another.
class Message:

    def __init__(self, sender, recipient, title, body):
        self.sender = sender
        self.recipient = recipient
        self.title = title
        self.body = body

    def setFrom(self, sender):
        self.sender = sender
    def getFrom(self):
        return self.sender

    def setTo(self, recipient):
        self.recipient = recipient
    def getTo(self):
        return self.recipient

    def setTitle(self, title):
        self.title = title
    def getTitle(self):
        return self.title

    def setBody(self, body):
        self.body = body
    def getBody(self):
        return self.body
