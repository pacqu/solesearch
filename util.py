import google, requests, beautifulsoup, urllib2, json

def getData():
    key= "AIzaSyBPILwQR9q7OBgW_NB2krK-Fc1PLNLJR0g"
    url = ""
    url = url%(key)
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    return r



