import User_Files.User
from User_Files.User import User
import User_Files.Profiles.UserProfiles
from User_Files.Profiles.UserProfiles import Profile
import User_Files.UserManager

import string

# menu for profiles
# input: loggedIn = User() object containing current logged in user; userManager = UserManager class for log-out operation
# returns: loggedIn
def profileMenu(loggedIn, userManager):
    profile = loggedIn.getProfile()

    while True:
        print("\n             Profile - " + loggedIn.getFirstName() + ' ' + loggedIn.getLastName() + "             ")
        print("Select a field of the profile to edit it. Additionally, select one of the other listed options.")
        print("""
        1. Title:      """ + str(profile.getTitle()) + """
        2. Major:      """ + str(profile.getMajor()) + """
        3. University: """ + str(profile.getUniversity()) + """
        4. About:      """ + str(profile.getAbout()) + """
        5. Experience: A) """ + str(profile.getExperience()[0]) + """
                       B) """ + str(profile.getExperience()[1]) + """
                       C) """ + str(profile.getExperience()[2]) + """
        6. Education:  """ + str(profile.getEducation()) + """
        
        9. Log-out
        0. Back to home page
        """)

        loggedIn.setProfile(profile)    # write new profile data to logged in User()

        try:
            newOption = int(input("Choice: "))
            print('\n')
            # Change title
            if newOption == 1:
                title = str(input("Enter a new title: "))
                profile.setTitle(title)
            # Change major
            elif newOption == 2:
                major = str(input("Enter a new major: "))
                major = string.capwords(major)  # Capitalizes first letter of each word
                profile.setMajor(major)
            # Change university
            elif newOption == 3:
                uni = str(input("Enter a new university: "))
                uni = string.capwords(uni)      # Capitalizes first letter of each word
                profile.setUniversity(uni)
            # Change about
            elif newOption == 4:
                about = str(input("Enter a new description: "))
                profile.setAbout(about)
            # Change work experience
            elif newOption == 5:
                print("Would you like to add, edit, or remove an experience?")
                print("""
                1. add
                2. edit
                3. remove

                0. Return to profile
                """)
                try:
                    option = int(input("Choice: "))
                    print('\n')
                    if option == 1:
                        profile = addExperience(profile)
                    elif option == 2:
                        profile = editExperience(profile)
                    elif option == 3:
                        profile = removeExperience(profile)
                    else:
                        print("Returning to profile...\n")
                except ValueError:
                    print("You provided a non-integer character.")
            # Change educational experience
            elif newOption == 6:
                print("Change your educational experience:\n")
                schoolName = str(input("Enter the name of the school: "))
                degree = str(input("Enter the highest degree earned: "))
                years = int(input("Enter the amount of years attended: "))
                profile.setEducation([schoolName, degree, years])
            # Log out
            elif newOption == 9:
                loggedIn = userManager.logOut()
                return loggedIn
            # Back to home page option
            elif newOption == 0:
                print("Returning to home page...")
                return loggedIn
        except ValueError:
            print("You provided a non-integer character.")


# add a new work experience to the profile
# input: profile = Profile() object from the current logged in user
# returns: profile = MODIFIED Profile() object from the current logged in user (unmodified if something occurrs)
def addExperience(profile):
    experienceA = profile.getExperience()[0]
    experienceB = profile.getExperience()[1]
    experienceC = profile.getExperience()[2]

    if experienceA != False and experienceB != False and experienceC != False:
        print("You have alrady listed the max amount of work experience!")
        return profile  # unmodified

    print("Add new work experience:\n")
    try:
        title = str(input("Enter the title given to you at your job: "))
        employer = str(input("Enter the name of your employer: "))
        startDate = str(input("Enter your start date for this position (MM-DD-YYYY): "))
        endDate = str(input("Enter your end date for this position (MM-DD-YYYY): "))
        location = str(input("Enter the location of your employment (ex: Detroit, MI): "))
        desc = str(input("Enter a few lines describing your duties during your employment: "))

        if experienceA == False:
            profile.setExperience([[title, employer, startDate, endDate, location, desc], experienceB, experienceC])
        elif experienceB == False:
            profile.setExperience([experienceA, [title, employer, startDate, endDate, location, desc], experienceC])
        else:
            profile.setExperience([experienceA, experienceB, [title, employer, startDate, endDate, location, desc]])

        return profile  # MODIFIED
    except Exception:
        print("An error occured while adding new work experience.")
        return profile  # unmodified


# remove an existing work experience from the profile
# input: profile = Profile() object from the current logged in user
# returns: profile = MODIFIED Profile() object from the current logged in user (unmodified if something occurrs)
def removeExperience(profile):
    experienceA = profile.getExperience()[0]
    experienceB = profile.getExperience()[1]
    experienceC = profile.getExperience()[2]

    if experienceA == False and experienceB == False and experienceC == False:
        print("You have no work experience to remove!")
        return profile  # unmodified

    try:
        choice = str(input("Select one of your work experiences to remove: "))
        if choice.upper() == 'A' and experienceA != False:
            profile.setExperience([False, experienceB, experienceC])
        elif choice.upper() == 'B' and experienceB != False:
            profile.setExperience([experienceA, False, experienceC])
        elif choice.upper() == 'C' and experienceC != False:
            profile.setExperience([experienceA, experienceB, False])
        else:
            print("Unable to remove work experience. Please try again later.")

        return profile # MODIFIED *or* unmodified
    except Exception:
        print("An error occured while removing existing work experience.")
        return profile  # unmodified


# change an existing work experience from the profile
# input: profile = Profile() object from the current logged in user
# returns: profile = MODIFIED Profile() object from the current logged in user (unmodified if something occurrs)
def editExperience(profile):
    experienceA = profile.getExperience()[0]
    experienceB = profile.getExperience()[1]
    experienceC = profile.getExperience()[2]

    try:
        choice = str(input("Select one of your work experiences to change: "))
        title = str(input("Enter the title given to you at your job: "))
        employer = str(input("Enter the name of your employer: "))
        startDate = str(input("Enter your start date for this position (MM-DD-YYYY): "))
        endDate = str(input("Enter your end date for this position (MM-DD-YYYY): "))
        location = str(input("Enter the location of your employment (ex: Detroit, MI): "))
        desc = str(input("Enter a few lines describing your duties during your employment: "))

        if choice.upper() == 'A':
            profile.setExperience([[title, employer, startDate, endDate, location, desc], experienceB, experienceC])
        elif choice.upper() == 'B':
            profile.setExperience([experienceA, [title, employer, startDate, endDate, location, desc], experienceC])
        elif choice.upper() == 'C':
            profile.setExperience([experienceA, experienceB, [title, employer, startDate, endDate, location, desc]])
        else:
            print("Unable to edit work experience. Please try again with a valid selection.")

        return profile # MODIFIED *or* unmodified
    except Exception:
        print("An error occured while editing existing work experience.")
        return profile  # unmodified