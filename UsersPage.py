###########################################
#####           DEPRECATED            #####
###########################################


# import pandas as pd

# class Users:
#     def __init__(self):
#         print("Loading Users page...")

#     # main function
#     # returns: string fullName = full name of found user; False if no user found
#     def userSearch(firstName, lastName):
#         while True:
#             # read data from .csv file
#             columns = ['Username', 'Password', 'First_Name', 'Last_Name']
#             data = pd.read_csv('users.csv', names = columns)
#             firstNames = data.First_Name.tolist()
#             lastNames = data.Last_Name.tolist()
#             # remove headers from lists so they are not read as an account combination
#             firstNames.remove("First_Name")
#             lastNames.remove("Last_Name")

#             # search for the user in the list
#             if firstName in firstNames and lastName == lastNames[firstNames.index(firstName)]:
#                 print("This person is a part of the InCollege system.")
#                 fullName = firstName + ' ' + lastName
#                 print("Returning to home page...")
#                 return fullName
#             else:
#                 print("This person is not yet a part of the InCollege system.")
#                 print("Returning to home page...")
#                 return False