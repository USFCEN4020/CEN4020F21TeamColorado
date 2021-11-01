import pytest
from testFileCore import set_keyboard_input, get_display_output, makeMultiInput

# Tested Managers
from User_Files.UserManager import UserManager
from User_Files.User import User

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
