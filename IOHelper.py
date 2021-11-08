# helper function to read True/False strings as booleans
# input: string = any string (preferrable containing 'True' or 'False')
# returns: True if 'True'; False if 'False'; string if not a boolean
def toBool(string):
    if string == "False":
        return False
    elif string == "True":
        return True
    else:
        return string