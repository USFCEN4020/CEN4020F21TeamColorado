import pytest
from User_Files.Friends.FriendList import FriendList
from User_Files.Friends.FriendRequest import FriendRequest
from User_Files.Friends.FriendRequestIO import FriendRequestIO
from User import User



# tests for FriendList methods
def testFriendList():
    # Test that the FriendList class can be instantiated
    fl = FriendList()
    assert fl

def testGetFriends():
    # Test that the getFriends method returns a list of friends
    fl = FriendList()
    assert isinstance(fl.getFriends(), list) != False

def testGetFriends_empty():
    # Test that the getFriends method returns an empty list if there are no friends
    fl = FriendList()
    assert fl.getFriends() == []

def testSetFriendList():
    # Test that the setFriendList method can set the friend list
    fl = FriendList()
    fl.setFriendList(['friend1', 'friend2'])
    assert fl.getFriends() == ['friend1', 'friend2']



# tests for FriendRequest methods
def testFriendRequest():
    # Test that the FriendRequest class can be instantiated
    fr = FriendRequest()
    assert fr

def testGetFrom():
    # Test that the getFrom method returns the from user
    usr = User()
    fr = FriendRequest()
    assert isinstance(fr.getFrom(), usr) != False

def testGetTo():
    # Test that the getTo method returns the to user
    usr = User()
    fr = FriendRequest()
    assert isinstance(fr.getTo(), usr) != False

def testAcceptFriend():
    # Test that the acceptFriend method can accept a friend request
    usr = User()
    fr = FriendRequest()
    fr.acceptFriend(usr)
    assert fr.getTo() == usr



# tests for FriendRequestIO methods
def testFriendRequestIO():
    # Test that the FriendRequestIO class can be instantiated
    fr = FriendRequestIO()
    assert fr != False

def testReadFriendRequest():
    # Test that the readFriendRequest method can read a friend request
    fr = FriendRequestIO()
    fr.readFriendRequest('test_files/friend_request.txt')
    assert fr.getFrom().getUsername() == 'Dummy'
    assert fr.getTo().getUsername() == 'SageKeesler'