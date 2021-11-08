import pandas as pd

def copyrightNotice():
    print("                             Copyright Notice                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

def aboutUs():
    print("                                 About Us                            ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

def accessibilityPage():
    print("                             Accessibility Page                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

def userAgreement():
    print("                             User Agreement                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

# returns: True, so that the user can access Guest Controls
def privacyPolicy():
    print("                             Privacy Policy                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)
    return True

def cookiePolicy():
    print("                             Cookie Policy                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

def brandPolicy():
    print("                             Brand Policy                       ")
    print("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Massa tempor nec feugiat nisl pretium 
        fusce id velit. Sem nulla pharetra diam sit amet nisl suscipit adipiscing bibendum.
        Tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi. Amet 
        consectetur adipiscing elit ut aliquam. Amet dictum sit amet justo donec enim diam 
        vulputate ut. Laoreet id donec ultrices tincidunt arcu non sodales. Dictum varius 
        duis at consectetur lorem donec. Vulputate sapien nec sagittis aliquam malesuada. 
        Amet venenatis urna cursus eget nunc scelerisque viverra mauris in. Aliquam
        vestibulum morbi blandit cursus risus at ultrices mi.\n
    """)

# lets a user toggle privacy settings
# input: loggedIn = User() object containing currently logged-in user
# returns: Settings() object containing updated settings of current user
def guestControls(loggedIn):
    setting2 = loggedIn.getSettings().getSetting2()
    setting3 = loggedIn.getSettings().getSetting3()
    setting4 = loggedIn.getSettings().getSetting4()
    while True:
        # set strings for menu
        if setting2 == False:
            setting2Str = "False"
        else:
            setting2Str = "True"
        if setting3 == False:
            setting3Str = "False"
        else:
            setting3Str = "True"
        if setting4 == False:
            setting4Str = "False"
        else:
            setting4Str = "True"

        print("                       Guest Controls                         ")
        print("Select one of the following options to toggle it...")
        print("""
            1. Receive email notifications: """ + setting2Str + """ [True/False]
            2. Recieve SMS notifications: """ + setting3Str + """ [True/False]
            3. Recieve relevant advertisements from InCollege: """ + setting4Str + """ [True/False]

            0. Return to previous page
        """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Toggle setting 1
            if newOption == 1:
                if setting2 == False:
                    setting2 = True
                else:
                    setting2 = False
                continue
            # Toggle setting 2
            elif newOption == 2:
                if setting3 == False:
                    setting3 = True
                else:
                    setting3 = False
                continue
            # Toggle setting 3
            elif newOption == 3:
                if setting4 == False:
                    setting4 = True
                else:
                    setting4 = False
                continue
            # exit function and return updated settings
            elif newOption == 0:
                loggedIn.getSettings().setSetting2(setting2)
                loggedIn.getSettings().setSetting3(setting3)
                loggedIn.getSettings().setSetting4(setting4)
                return loggedIn.getSettings()
        except ValueError:
            print("You provided a non-integer value.")

# lets a user change language setting
# input: loggedIn = User() object containing currently logged-in user
# returns: Settings() object containing updated settings of current user
def changeLanguage(loggedIn):
    language = loggedIn.getSettings().getLanguage()
    while True:
        print("                       Language Select                         ")
        print("Select one of the currently available languages...")
        print("""
            Current Language: '""" + language + """'
            1. English [EN]
            2. Spanish [ES]

            0. Return to previous page
        """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Toggle setting 1
            if newOption == 1:
                language = "EN"
            # Toggle setting 2
            elif newOption == 2:
                language = "ES"
            # exit function and return updated settings
            elif newOption == 0:
                loggedIn.getSettings().setLanguage(language)
                return loggedIn.getSettings()
        except ValueError:
            print("You provided a non-integer value.")

# main function containing all of the Important Links
# input: loggedIn = string containing full name of logged in user, or False if empty (not logged in)
# NO RETURN VALUE: all functions are print statements full of text blocks
def importantLinksMenu(loggedIn):
    while True:
        print("                       InCollege - Important Links                         ")
        print("Please select one of the following options to view the associated document.")
        print("""
            1. Copyright Notice
            2. About
            3. Accessibility
            4. User Agreement
            5. Privacy Policy
            6. Cookie Policy
            7. Brand Policy

            8. Guest Controls (must read and accept Privacy Policy to access)
            9. Languages

            0. Return Home
        """)
        try:
            newOption = int(input("Choice: "))
            print()
            # Copyright Notice option
            if newOption == 1:
                copyrightNotice()
            # About option
            elif newOption == 2:
                aboutUs()
            # Accessibility option
            elif newOption == 3:
                accessibilityPage()
            # User Agreement option
            elif newOption == 4:
                userAgreement()
            # Privacy Policy option
            elif newOption == 5:
                loggedIn.getSettings().setSetting1(privacyPolicy())   # setting 1 = True
            # Cookie Policy option
            elif newOption == 6:
                cookiePolicy()
            # Brand Policy option
            elif newOption == 7:
                brandPolicy()
            # Guest Controls option
            elif newOption == 8 and not loggedIn:
                print("You must be logged in to access user settings!\n")
            elif newOption == 8 and loggedIn:
                policyAccepted = loggedIn.getSettings().getSetting1()
                # check if privacy policy was viewed
                if not policyAccepted:
                    print("You must view and accept the Privacy Policy first.\n")
                else:
                    guestControls(loggedIn)
            # Languages option
            elif newOption == 9 and not loggedIn:
                print("You must be logged in to access user settings!\n")
            elif newOption == 9 and loggedIn:
                changeLanguage(loggedIn)
            # Return home option
            elif newOption == 0:
                print("Returning to home page...")
                break
        except ValueError:
            print("You provided a non-integer value.")
    