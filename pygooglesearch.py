from pygoogle import pygoogle
query = raw_input("What do you want to search for ? >> ")
g = pygoogle(query)
g.pages = 5
print '*Found %s results*'%(g.get_result_count())
print type(g.get_urls())
slist=g.get_urls()
for i in slist:
	print i+"\n"
'''
import urllib2
import urllib
import json
import pprint
query = raw_input("What do you want to search for ? >> ")
query = urllib2.quote(query)
key='AIzaSyDLutTaTYonllml54cD1vy9jHva-fOep1I'
data = urllib2.urlopen('https://www.googleapis.com/customsearch/v1?key='+key+'&cx=017576662512468239146:omuauf_lfve&q='+query)
data = json.load(data)
print type(data)
#pprint.PrettyPrinter(indent=4).pprint(data['items'][0])
#print data
print data['url'],'\n'
'''
