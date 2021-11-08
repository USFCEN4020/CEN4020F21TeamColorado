import User_Files
from User_Files.User import User
from User_Files.UserManager import UserManager
import User_Files.Friends
from User_Files.Friends.FriendHandler import FriendHandler
from User_Files.Friends.FriendsList import FriendsList
from User_Files.Friends.FriendRequest import FriendRequest

# initiate friend handler to deal with friend-related operations
friendHandler = FriendHandler()

# menu for friends-related operations
# input: loggedIn = User() object for current logged in user; userManager = UserManager() from main()
def friendsMenu(loggedIn, userManager):

    while True:
        print("\n           Friends Menu           ")
        print("Select one of the following options.")
        print("""
            1. Find a friend
            2. View friends list
            3. Manage friends
            4. Pending friend requests

            0. Exit
        """)
        try:
            newOption = int(input("Choice: "))
            print('\n')
            # Find a friend option
            if newOption == 1:
                searchMenu(loggedIn, userManager)
            # View friends option
            elif newOption == 2:
                friendHandler.displayFriends(loggedIn.getFriendsList().getFriends())
            # Manage friends option
            elif newOption == 3:
                userManager = manageFriends(loggedIn, userManager)
            # Manage requests option
            elif newOption == 4:
                userManager.userList = manageRequests(loggedIn, userManager.userList)
            # Back to home page option
            elif newOption == 0:
                print("Returning to home page...")
                return userManager
        except ValueError:
            print("You provided a non-integer character.")

        # TODO: Display pending friend requests, displaying both outgoing and incoming requests


# menu for searching for and adding friends
# input: loggedIn = User() object for current logged in user; userManager = UserManager() class from main()
# returns: updated userManager
def searchMenu(loggedIn, userManager):
    
    while True:
        print("\n           Friend Search Menu           ")
        print("Select a method for searching for a friend.")
        print("""
            1. Search by last name
            2. Search by university
            3. Search by major

            0. Back to menu
        """)
        try:
            newOption = int(input("Choice: "))
            print('\n')
            # Search by last name
            if newOption == 1:
                lastName = str(input("Enter the last name of the user you would like to search for: "))
                found = userManager.findUsersByName(lastName)
            # Search by university
            elif newOption == 2:
                university = str(input("Enter the university of the user you would like to search for: "))
                found = userManager.findUsersByUni(university)
            # Search by major
            elif newOption == 3:
                major = str(input("Enter the major of the user you would like to search for: "))
                found = userManager.findUsersByMajor(major)
            # Back to home page option
            elif newOption == 0:
                print("Returning to menu...")
                return userManager

            # if the search returned users, print them and allow the user to select people to send requests
            if found:
                userManager.userList = addFriend(loggedIn, userManager.userList, found)     # update userList
            else:
                print("No users found.")

        except ValueError:
            print("You provided a non-integer character.")


# menu for adding friends by using the friendHandler
# input: loggedIn = current logged in User() object
# input: userList = list of User()s in the system from userManager
# input: foundUsers = list of User() objects found from the friend search function
# returns: updated userList
def addFriend(loggedIn, userList, foundUsers):
    print("\nSelect a user to send them a friend request:")
    # check if foundUsers contains a single object
    if len(foundUsers) == 1:
        print("1. " + str(foundUsers[0].getFirstName()) + ' ' + str(foundUsers[0].getLastName()) + " (" + str(foundUsers[0].getUsername()) + ")")
        print("\n0. Go back")
        try:
            print('\n')
            choice = int(input("Choice: "))
            if choice == 1:
                friendRequest = friendHandler.createRequest(loggedIn.getUsername(), foundUsers[0].getUsername())
                requestSuccess = friendHandler.sendRequest(friendRequest, userList)
                if requestSuccess:
                    userList = requestSuccess
            elif choice == 0:
                print("Returning to menu...")
                return userList
            else:
                print("Invalid selection, returning to menu...")
        except ValueError:
            print("You provided a non-integer character.")
    # boiler-plate code for if foundUsers is a list
    else:
        i = 1
        for user in foundUsers:
            print(str(i) + ". " + str(user.getFirstName()) + ' ' + str(user.getLastName()) + " (" + str(user.getUsername()) + ")\n")
            i += 1
        print("\n0. Go back")
        try:
            print('\n')
            choice = int(input("Choice: "))
            # send request to selected user (or exit menu) if valid selection
            if choice <= len(foundUsers) + 1 and choice >= 0:
                if choice == 0:
                    print("Returning to menu...")
                    return userList
                else:
                    friendRequest = friendHandler.createRequest(loggedIn.getUsername(), foundUsers[choice-1].getUsername())
                    requestSuccess = friendHandler.sendRequest(friendRequest, userList)
                    if requestSuccess:
                        userList = requestSuccess
            else:
                print("Invalid selection, returning to menu...")
        except ValueError:
            print("You provided a non-integer character.")

    return userList


# menu to manage friends
# input: loggedIn = User() object for current logged in user; userManager = UserManager() class from main()
# returns: updated userManager
def manageFriends(loggedIn, userManager):
    
    while True:
        print("Select a user to see available options:")
        friendsDisplay = friendHandler.displayFriends(loggedIn.getFriendsList().getFriends())
        if not friendsDisplay:
            print("Returning to menu...")
            return userManager

        print("\n0. Go back")
        try:
            print('\n')
            # select friend to manage
            choice = int(input("Choice: "))
            if choice <= len(loggedIn.getFriendsList().getFriends()) + 1 and choice >= 0:
                # return to menu
                if choice == 0:
                    print("Returning to menu...")
                    return userManager
                else:
                    # find selected user in list
                    for user in userManager.userList:
                        if user.getUsername() == loggedIn.getFriendsList().getFriends()[choice-1]:
                            friend = user
                            break
                    print(str(friend.getFirstName()) + ' ' + str(friend.getLastName()) + " (" + str(friend.getUsername()) + ")\n")
                    print("1. Delete")
                    # check if selected friend has a profile
                    if friendHandler.checkForProfile(friend.getProfile()):
                        print("2. View Profile")
                    print("\n0. Go back")
                    try:
                        print('\n')
                        option = int(input("Choice: "))
                        # delete a friend (and update userManager if successful)
                        if option == 1:
                            result = friendHandler.removeFriend(loggedIn, friend.getUsername(), userManager.userList)
                            if result:
                                userManager.userList = result
                        # view a profile (if one exists)
                        elif option == 2 and friendHandler.checkForProfile(friend.getProfile()):
                            userManager.displayProfile(friend.getProfile())
                        # return home
                        elif option == 0:
                            print("Returning to menu...")
                            return userManager
                    except ValueError:
                        print("You provided a non-integer character.")
        except ValueError:
            print("You provided a non-integer character.")


# menu to manage friends
# input: loggedIn = User() object for current logged in user; userList = list of User()s in the system from userManager
# returns: updated userList
def manageRequests(loggedIn, userList):

    while True:
        recievedRequests = friendHandler.displayRequests(loggedIn.getFriendsList().getRequests())
        # return if no requests or only outgoing requests
        if not recievedRequests:
            print("Returning to menu...")
            return userList
        
        print("Select a request from Recieved Friend Requests to accept or decline it.")
        print("\n0. Go back")
        try:
            print('\n')
            # select request to manage
            choice = int(input("Choice: "))
            if choice <= len(recievedRequests) + 1 and choice >= 0:
                # return to menu
                if choice == 0:
                    print("Returning to menu...")
                    return userList
                else:
                    # find selected user in list
                    for user in userList:
                        if user.getUsername() == recievedRequests[choice-1]:
                            try:
                                selection = str(input("Accept this friend request? (y/n): "))
                                # accept/decline friend request
                                if selection.lower() == 'y':
                                    userList = friendHandler.acceptRequest(loggedIn, user.getUsername(), userList)
                                elif selection.lower() == 'n':
                                    userList = friendHandler.declineRequest(loggedIn, user.getUsername(), userList)
                                else:
                                    print("Invalid selection. Returning to requests...")
                                break
                            except ValueError:
                                print("You provided a non-integer character.")
        except ValueError:
            print("You provided a non-integer character.")