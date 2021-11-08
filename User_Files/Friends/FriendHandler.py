import User_Files.Friends.FriendsList
from User_Files.Friends.FriendsList import FriendsList
import User_Files.Friends.FriendRequest
from User_Files.Friends.FriendRequest import FriendRequest


# class to handle all friend-related operations, but NOT store data (in the class itself)
class FriendHandler:

    # creates a friend request object
    # input: sender = string containing username of User() sending the request
    # input: recipient = string containing username of User() who is recieving the request
    # returns: friendRequest = FriendRequest() object
    def createRequest(self, sender, recipient):
        friendRequest = FriendRequest(sender, recipient)
        return friendRequest


    # sends a given friend request to its recipient
    # input: request = FriendRequest() object to be sent; userList = list of User() objects in the system
    # returns: updated userList; False if failed to find sender/recipient
    def sendRequest(self, request, userList):
        sent = False
        recieved = False
        for user in userList:
            # find recipient
            if request.getRecipient() == user.getUsername():
                # append request to recipient's friend list
                recipientRequests = user.getFriendsList().getRequests()
                recipientRequests.append([request.getSender(), "recieved"])
                user.getFriendsList().setRequests(recipientRequests)
                recieved = True
            # find sender
            elif request.getSender() == user.getUsername():
                # append request to sender's friend list
                senderRequests = user.getFriendsList().getRequests()
                senderRequests.append([request.getRecipient(), "pending"])
                user.getFriendsList().setRequests(senderRequests)
                sent = True
        # end for

        if sent == False:
            print("Failed to send request. Please try again later.")
            return False
        elif recieved == False:
            print("Failed to send request. Recipient may not exist.")
            return False
        else:
            print("Request sent!")
            return userList


    # accepts a friend request, adding users to each other's friend lists
    # input: loggedIn = User() object containing current logged in user
    # input: userList = list of User() objects in the system
    # input: sender = string containing username of user who sent request
    # returns: updated userList; False if an error is thrown
    def acceptRequest(self, loggedIn, sender, userList):
        try:
            for user in userList:
                # find current user
                if user.getUsername() == loggedIn.getUsername():
                    friendsList = user.getFriendsList().getFriends()
                    requestList = user.getFriendsList().getRequests()
                    # remove request / add friend
                    requestList.remove([sender, "recieved"])
                    friendsList.append(sender)
                    # update user
                    user.getFriendsList().setFriends(friendsList)
                    user.getFriendsList().setRequests(requestList)
                # find sender of the request
                elif user.getUsername() == sender:
                    senderFriends = user.getFriendsList().getFriends()
                    senderRequests = user.getFriendsList().getRequests()
                    # remove request / add friend
                    senderRequests.remove([loggedIn.getUsername(), "pending"])
                    senderFriends.append(loggedIn.getUsername())
                    # update user
                    user.getFriendsList().setFriends(senderFriends)
                    user.getFriendsList().setRequests(senderRequests)
            # end for
            print("Friend request accepted! You and " + sender + " are now friends.\n")
            return userList
        except Exception:
            print("An error occurred while accepting a friend request. Please try again later.")
            return False


    # declines a friend request, removing it from both user's requests lists
    # input: loggedIn = User() object containing current logged in user
    # input: userList = list of User() objects in the system
    # input: sender = string containing username of user who sent request
    # returns: updated userList; False if an error is thrown
    def declineRequest(self, loggedIn, sender, userList):
        try:
            for user in userList:
                # find current user
                if user.getUsername() == loggedIn.getUsername():
                    requestList = user.getFriendsList().getRequests()
                    # remove request
                    requestList.remove([sender, "recieved"])
                    # update user
                    user.getFriendsList().setRequests(requestList)
                # find sender of the request
                elif user.getUsername() == sender:
                    senderRequests = user.getFriendsList().getRequests()
                    # remove request
                    senderRequests.remove([loggedIn.getUsername(), "pending"])
                    # update user
                    user.getFriendsList().setRequests(senderRequests)
            # end for
            print("Request successfully denied.\n")
            return userList
        except Exception:
            print("An error occurred while declining a friend request. Please try again later.")
            return False


    # deletes a friend, removing it from both user's friends lists
    # input: loggedIn = User() object containing current logged in user
    # input: userList = list of User() objects in the system
    # input: friend = string containing username of friend to be removed
    # returns: updated userList; False if an error is thrown
    def removeFriend(self, loggedIn, friend, userList):
        try:
            for user in userList:
                # find current user
                if user.getUsername() == loggedIn.getUsername():
                    friendsList = user.getFriendsList().getFriends()
                    # remove friend
                    friendsList.remove(friend)
                    # update user
                    user.getFriendsList().setFriends(friendsList)
                # find sender of the request
                elif user.getUsername() == friend:
                    senderFriends = user.getFriendsList().getFriends()
                    # remove friend
                    senderFriends.remove(loggedIn.getUsername())
                    # update user
                    user.getFriendsList().setFriends(senderFriends)
            # end for
            print(friend + " successfully removed from friend list.\n")
            return userList
        except Exception:
            print("An error occurred while deleting a friend. Please try again later.")
            return False


    # display a list of friends
    # input: friends = list() containing list of friends (!!!NOT FriendsList() OBJECT!!!)
    # returns: True if friends printed; False if no friends :(
    def displayFriends(self, friends):
        if not friends:
            print("There are no friends to display :(")
            return False
        
        # loop through friends and display each one
        print("Friends: ")
        if len(friends) == 1:
            print("1. " + str(friends[0]))
        else:
            i = 1
            for friend in friends:
                print(str(i) + ". " + str(friend))
                i += 1
        return True


    # sort and display a list of requests
    # input: friends = list() containing list of requests (!!!NOT FriendRequest() OBJECT!!!)
    # returns: recievedRequests = list of requests marked as "recieved"; False if no requests of any kind
    def displayRequests(self, requests):
        if not requests:
            print("You have no pending or outgoing friend requests.")
            return False

        pendingRequests = list()
        recievedRequests = list()
        # loop through requests and sort them by type
        for name, request in requests:
            if "pending" in request:
                pendingRequests.append(name)
            elif "recieved" in request:
                recievedRequests.append(name)

        # loop through sorted requests and print them
        if pendingRequests:
            print("Pending Friend Requests: ")
            if len(pendingRequests) == 1:
                print("1. " + str(pendingRequests[0]))
            else:
                i = 1
                for request in pendingRequests:
                    print(str(i) + ". " + str(request))
                    i += 1
            print('\n')
        if recievedRequests:
            print("Recieved Friend Requests: ")
            if len(recievedRequests) == 1:
                print("1. " + str(recievedRequests[0]))
            else:
                i = 1
                for request in recievedRequests:
                    print(str(i) + ". " + str(request))
                    i += 1
            print('')

        return recievedRequests


    # displays notification indicating how many friend requests are pending
    # input: user = User() object to display notification to
    # returns: message = string containing notification; False if no pending requests
    def friendNotif(self, user):
        requests = user.getFriendsList().getRequests()
        recievedRequests = []
        for request in requests:
            if "recieved" in request:
                recievedRequests.append(request)

        if not recievedRequests:
            return False
        
        message = "(You have " + str(len(requests)) + " pending friend request(s).)"
        return message


    # helper function to cut down boiler-plate code for checking if a profile has been created
    # input: profile = Profile() object for a given user
    # returns: True if profile exists; False if not
    def checkForProfile(self, profile):
        if not profile.getTitle() and not profile.getMajor() and not profile.getUniversity() and not profile.getAbout() and profile.getExperience() == [False, False, False] and not profile.getEducation():
            return False
        else:
            return True