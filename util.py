import google, requests, bs4, urllib2, json


def getPages(query):
    '''
    Finds the Resulting Pages from and inputted query
    Parameter: String Query to find results for
    Returns: List of URLs of Resulting Pages
    '''
    res = google.search(query,num=10,start=0,stop=10)
    results = []
    appending = res.next()
    for i in range(10): 
        results.append(res.next())
    return results



def getPageString(u):
    '''
    Gets Page Contents as a String
    Paramater: String of URL of Page
    Returns: String of all HTML in Page
    '''
    url = urllib2.urlopen(u)
    page = url.read()
    #print page
    soup = bs4.BeautifulSoup(page,'html.parser')
    #raw = soup.get_text(page)
    return soup.prettify()
   
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

r = getPages("pi")
print getPageString(r[0])
