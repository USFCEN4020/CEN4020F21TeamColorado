import pytest
from testFileCore import set_keyboard_input, get_display_output, makeMultiInput

# Tested User Managers Components
from User_Files.UserManager import UserManager
from User_Files.User import User

# Tested Message Managers Components
from User_Files.Messages.MessageHandler import MessageHandler
from User_Files.Messages.Message import Message

# User Manager Tests
def testUserLogIn():
    # Precept for the test configuration
    set_keyboard_input(["SageKeesler", "Password#123"])
    # Preliminary run of precepts
    testUser = UserManager.logIn()
    output = get_display_output()
    # Test Asserts
    assert output == ["     Log-In Page      \n",
                      "Username: ",
                      "Password: ",
                      "Login Successful! Returning to home page..."]
    assert testUser != False

def testSearch():
    set_keyboard_input(['1', 'Jameson', '2'])
    testUser = None
    UserManager.userSearch(testUser)
    output = get_display_output()

    assert output == ["     Search-A-User Page      \n",
                      "     Select the search option      \n",
                      "     1. Search by Last Name        ",
                      "     2. Search by University       ",
                      "     3. Search by Major            \n",
                      "Choice: "]
    assert testUser != False
    assert testUser != None

def testCreateAccount():
    # change the argument array for this function to test with different values for inputs
    set_keyboard_input(["username", "Pass123!", "First", "Last"])
    # call the function to be tested
    UserManager.createAccount()
    output = get_display_output()
    # test
    assert output == ["Provide the username for the new account: ",
                      "Provide password of the new account: ",
                      'Valid Password',
                      "Provide your first name: ",
                      "Provide your last name: ",
                      "Account successfully created. Returning home...\n"
                      ]

# Message Handler Tests
def testCreateMessage():
    set_keyboard_input(["This is a test title", "this is a test message"])
    testUser1 = User('Tester1','Password#123','James','Smith', 'Plus')
    testUser2 = User('Teste2', 'Password#123', 'John', 'Doe', 'Plus')
    testMessage = MessageHandler.createMessage(testUser1, testUser2)
    output = get_display_output()
    assert output == ["Enter the title of your message:\n", "Write your message below:\n"]
    assert testMessage != False

def testSendMessage():
    testmessage = Message('Tester1', 'Tester2', 'Test title', 'Test message')
    testUser1 = User('Tester1', 'Password#123', 'James', 'Smith', 'Plus')
    testUser2 = User('Tester2', 'Password#123', 'John', 'Doe', 'Plus')
    testUserList = list()
    testUserList.append(testUser1)
    testUserList.append(testUser2)
    assert MessageHandler.sendMessage(testmessage,testUserList) != False
