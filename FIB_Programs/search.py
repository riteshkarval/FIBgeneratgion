def gettext(url):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    for script in soup(["script", "style"]):
        script.extract()   
    # rip it out
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
    slist=sentdec.tokenize(text.strip())
    return slist
import nltk
import re
import nltk.data
import sys
from nltk.corpus import stopwords
import urllib
import json
import urllib
from bs4 import BeautifulSoup

url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q="

query = raw_input("What do you want to search for ? >> ")

query = urllib.quote(query)

response = urllib.urlopen (url + query ).read()

data = json.loads ( response )
#print data['"moreResultsUrl']
#print str(data)

results = data [ 'responseData' ] [ 'results' ]
print type(results)
string=[]
for result in results:
    title = result['title']
    url = result['url']
    #print ( title + '; ' + url )
    string=string+gettext(url)
for s in string:
    print s,'\n'
    
