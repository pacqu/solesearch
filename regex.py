import re


def whoRegex():
    '''
    Gets the regular expression for a name
    Parameter: None
    Returns: String regular expression for that name
    '''
    regExp = "[A-Z]\w* [A-Z]\w*"
    return regExp

def whenRegex():
    '''
    Gets the regular expression for a time
    Parameter: None
    Returns: String regular expression for the date
    '''
    regExp = "(?(/*)|{1,2}/{1,2}/{2,4})"
    pass

def whereRegex():
    '''
    Gets the regular expression for a location
    Parameter: None
    Returns: String regular expression for the date
    '''
    pass
