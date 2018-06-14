import re

def validPassword(password):
    rgString = '(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
    return bool(re.match(rgString,password))