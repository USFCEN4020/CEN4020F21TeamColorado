from User import User
from Message import Message

class MessageHandler:

    # function to create a message
    # input: loggedIn: User() object containing the current logged-in user
    # input: recipient: User() object containing the user who is recieving the message
    # returns: message: Message() object that was created; False: the users are not friends and the current user is not a Plus member
    def createMessage(self, loggedIn, recipient):
        # check that the two users are friends and/or the current user is a Plus member
        if (recipient.getUsername() not in loggedIn.getFriends().getFriendList()) and (loggedIn.getStatus() != "Plus"):
            print("I'm sorry, you are not friends with that person.\n")
            return False
        
        title = str(input("Enter the title of your message:\n"))
        body = str(input("Write your message below:\n"))
        message = Message(loggedIn.getUsername(), recipient.getUsername(), title, body)

        return message


    # adds a created message to recipients' inbox
    # input: message = Message() object being sent; userList = list of registered users
    # returns: True, if message successfully sent; False, if message fails to send
    def sendMessage(self, message, userList):
        # find recipient in userList
        for user in userList:
            if message.getTo() == user.getUsername():
                user.inbox.append(message)   # append message object to user's inbox
                return True
            
        print("There was an issue sending the message. Please try again later.\n")
        return False


    # deletes the selected message for the current user
    # input: loggedIn = User() object containing the current logged in user; title = String containing the title of the message to be deleted
    # returns: True, if message delete successful; False, if unsuccessful
    def deleteMessage(self, loggedIn, title):
        # find message in inbox by title
        for message in loggedIn.inbox:
            if message.getTitle() == title:
                loggedIn.inbox.remove(message)   # remove message from the user's inbox
                return True

        print("There was an issue deleting the message. Please try again later.\n")
        return False


    # displays all messages (by title) in the current user's inbox
    # input: loggedIn = User() object containing the current logged in user
    # returns: len(inbox) = integer containing the length of the current user's inbox; False if inbox is empty
    def displayInbox(self, loggedIn):
        # check if inbox is empty
        if not loggedIn.inbox:
            print("Your inbox is empty!")
            return False

        # loop through inbox and display message titles
        i = 1
        for message in loggedIn.inbox:
            print(i + ". " + message.getTitle())
            i += 1
        return len(loggedIn.inbox)