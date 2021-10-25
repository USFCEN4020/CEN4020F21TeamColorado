###########################################
#####           DEPRECATED            #####
###########################################


#import pandas as pd
#
#class CreateAccount:
#    def __init__(self):
#        print("Loading Creating Account page...")
#    # # adds account to .csv file
#    # # returns: True if account add was successful; False if account could not be added
#    def addAcc(self, username, name, surname, password):
#        # read account info from file
#        columns = ['Username', 'Password', 'First_Name', 'Last_Name']
        # data = pd.read_csv('users.csv', names = columns)
        # userList = data.Username.tolist()
        # passList = data.Password.tolist()
        # firstNames = data.First_Name.tolist()
        # lastNames = data.Last_Name.tolist()
        # # remove headers from lists so they are not read as an account combination
        # userList.remove("Username")
        # passList.remove("Password")
        # firstNames.remove("First_Name")
        # lastNames.remove("Last_Name")

        # # check to see if max accounts has been reached
        # if len(userList) >= 6:
        #     print("The maximum amount of accounts has already been made!")
        #     print("Returning to home page...")
        #     return False
        # else:
        #     # append retrieved data to list
        #     userList.append(username)
        #     passList.append(password)
        #     firstNames.append(name)
        #     lastNames.append(surname)

        #     # write to user.csv
        #     dictionary = {'Username':userList, 'Password':passList, 'First_Name':firstNames, 'Last_Name':lastNames}
        #     df = pd.DataFrame(dictionary)
        #     df.to_csv('users.csv', index=False)

        #     # read userSettings.csv
        #     columns = ['Username', 'Accept_Privacy_Policy', 'email', 'sms', 'ads', 'language']
        #     data = pd.read_csv('userSettings.csv', names = columns)
        #     userList = data.Username.tolist() # from userSettings.csv
        #     settings1 = data.Accept_Privacy_Policy.tolist()
        #     settings2 = data.email.tolist()
        #     settings3 = data.sms.tolist()
        #     settings4 = data.ads.tolist()
        #     languages = data.language.tolist()
        #     userList.remove("Username")
        #     settings1.remove("Accept_Privacy_Policy")
        #     settings2.remove("email")
        #     settings3.remove("sms")
        #     settings4.remove("ads")
        #     languages.remove("language")

        #     userList.append(username)
        #     settings1.append(False)
        #     settings2.append(False)
        #     settings3.append(False)
        #     settings4.append(False)
        #     languages.append("EN")

        #     # create settings config and write to userSettings.csv
        #     dictionary = {'Username', 'Accept_Privacy_Policy', 'email', 'sms', 'ads', 'language'}

        #     print("Account has successfully been created! Returning to home page...")
        #     return True
