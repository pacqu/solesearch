import google, bs4, urllib2, regex 

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
    Gets Page HTML Content as a String
    Paramater: String of URL of Page
    Returns: String of all HTML in Page
    '''
    #print u
    try:
        url = urllib2.urlopen(u)
        page = url.read()
        soup = bs4.BeautifulSoup(page,'html.parser')
        text = soup.get_text()
        return text
    except:
        #print 'Couldnt Open'
        return ''

def getPStrings(query):
    '''
    Gets List of PageStrings
    Parameter: String Query to find results
    Returns: List of Strings of HTML of Page Results
    '''
    urllist=getPages(query)
    PStrings = []
    for u in urllist:
        PStrings.append(getPageString(u))
    return PStrings

def getWhoResults(query):
    '''
    Gets Answer based on the 'Who' Query provided
    Parameter: String Query
    Returns: String Result
    '''
    pages = getPStrings(query)
    
    namelist = []
    for page in pages:
        namelist += regex.getNames(page)
    
    #print namelist
    #print regex.countNames(namelist)
    return regex.highestName(regex.countNames(namelist))

#r = getPages("pi")
#hi = getPageString(r[0])
#print removeStopWords(hi)

print getWhoResults("Who is the Principal of Stuyvesant High School?")
