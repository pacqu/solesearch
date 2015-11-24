import google, requests, beautifulsoup, urllib2, json, re

def getData():
    key= "AIzaSyBPILwQR9q7OBgW_NB2krK-Fc1PLNLJR0g"
    url = ""
    url = url%(key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r

def findName(checkList):
    '''Find the query using regular expression and google
    Parameters: list of pages to look through
    Return: Results of the search in a list form
    '''
    #This is supposed to look for a name
    #legit does not work 
    result = []
    regExp = ""
    for i in checkList:
        match = re.search(regExp, i)
        if match:
            for value in match.group():
                result.append(value)
    return result

