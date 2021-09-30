###########################################
#####           DEPRECATED            #####
###########################################


# import pandas as pd

# class Login:
#     def __init__(self):
#         print("Loading Login page...")
    
#     # main LogIn function
#     # input: loggedIn = string containing logged-in user's name, or False if empty (nobody logged in)
#     # returns: string fullName = full name of user who logged in, False if login unsuccessful
#     def getLoginInput(self, loggedIn):
#         # log user out if they are already logged in
#         if loggedIn:
#             print("You have successfully been logged out of your account.")
#             print("Returning to home page...")
#             return False
#         else:
#             # read columns from 'users.csv' to list; read using PANDAS library
#             columns = ['Username', 'Password', 'First_Name', 'Last_Name']
#             data = pd.read_csv('users.csv', names = columns)
#             userList = data.Username.tolist()
#             passList = data.Password.tolist()
#             firstNames = data.First_Name.tolist()
#             lastNames = data.Last_Name.tolist()
#             # remove headers from lists so they are not read as an account combination
#             userList.remove("Username")
#             passList.remove("Password")
#             firstNames.remove("First_Name")
#             lastNames.remove("Last_Name")


#             print("     Log-In Page      \n")
#             while True:
#                 username = input("Username: ")
#                 password = input("Password: ")
#                 if username in userList and password == passList[userList.index(username)]:
#                     print("Login Successful! Returning to home page...")
#                     fullName = firstNames[userList.index(username)] + ' ' + lastNames[userList.index(username)]
#                     return fullName
#                 else:
#                     print("Incorrect username/password. Please try again.")
#                     continue
