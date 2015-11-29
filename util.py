import google, bs4, urllib2,
from stop_words import get_stop_words


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
    url = urllib2.urlopen(u)
    page = url.read()
    #print page
    soup = bs4.BeautifulSoup(page,'html.parser')
    #raw = soup.get_text(page)
    return soup.prettify()

def getPStrings(query):
    '''
    Gets List of PageStrings
    Parameter: String Query to find results
    Returns: List of Strings of HTML of Page Results
    '''
    urllist=getPages(query)
    PStrings = []
    for u in urllist:
        PStrings.append(u)
    return PStrings

def removeStopWords(page):
    '''
    Returns Page's HTML Contents with stop words removed
    Parameter: String page that hold HTML of a page
    Returns: String of Page with Stop Words removed
    '''
    stopwords = []
    with open("stopwords.txt","r") as f:
        for line in f:
            stopwords.append(line)
    words = page.split(" ")
    for word in words:
        if word in stopwords:
            stopwords.remove(word)
    newPage = words.join(" ")
    return newPage

r = getPages("pi")
#print getPageString(r[0])
