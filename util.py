import google, requests, bs4, urllib2, json

'''
Returns List of Result URLs from Google Query 
'''
def getQueries(query):
    res = google.search(query,num=10,start=0,stop=10)
    results = []
    l = dir(res)
    return l
'''
    for r in res:
        results.append(r)
    return results
'''


'''
Returns Contents of Page as a String
'''
def getPageString(u):
    url = urllib2.urlopen(u)
#print url
    page = url.read().decode('ascii')
#print page
    soup = bs4.BeautifulSoup(page,"html.parser")
    raw = soup.get_text(page)
    return raw
    
#print  getQueries("hi")
#print getPageString(r[0])

'''
idk if still want this
def getData():
    key= "AIzaSyBPILwQR9q7OBgW_NB2krK-Fc1PLNLJR0g"
    url = ""
    url = url%(key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r
'''

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

