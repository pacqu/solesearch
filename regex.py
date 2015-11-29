import re


def whoRegex():
    '''
    Gets the regular expression for a name
    Parameter: None
    Returns: String regular expression for that name
    '''
    regExp = "[A-Z][a-z]+ [A-Z][a-z]+"
    return regExp

def whenRegex():
    '''
    Gets the regular expression for a time
    Parameter: None
    Returns: String regular expression for the date
    Note:
    Format should be:
    03/05/1992, 3/5/1992, March 5, 1992 etc.
    '''
    regExp = "[0-9]{1,2}[-/][0-9]{1,2}[-/][0-9]{2,4}|[A-Z][a-z]+ [0-9]{0,2}[a-z]{2}, [0-9]{2,4}"
    return regExp

def whereRegex():
    '''
    Gets the regular expression for a location
    Parameter: None
    Returns: String regular expression for the date
    '''
    pass



def getNames(input):
    '''
    Gets list of names that appear in inputted string
    Parameter: String of Text
    Returns: List of Names
    '''
    return re.findall(whoRegex(), input)

def countNames(namelist):
    '''
    Gets the number of times a name appears in a list
    Parameter: List of Names
    Returns: Dictionary where keys are the names, corresponding values are number of times name appears
    ''' 
    namedict = {}
    for name in namelist:
        if (namedict.has_key(name)):
            namedict[name] += 1
        else:
            namedict[name] = 1
    return namedict
        

def highestName(namedict):
    '''
    Gets the name the appeared the most frequently
    Parameter: Dictionary where keys are names, corresponding values is frequency of names
    Returns: Name with highest frequency
    '''
    highname = namedict.keys()[0]
    for name in namedict.keys():
        if namedict.get(name) > namedict.get(highname):
            highname = name
    return highname

#input = "Peter Parker the woah Peter Parker hey Uncle nasty Ben Uncle Ben wow Peter Parker testing test. Uncle Ben Peter Parker Uncle Ben Peter Parker Uncle Ben Aunt Lily"
#names = getNames(input)
#dict =  countNames(names)
#print dict
#print highestName(dict)
