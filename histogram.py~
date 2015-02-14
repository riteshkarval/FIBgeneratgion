import nltk
import nltk.data
import sys
from nltk.corpus import stopwords
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
f = open(sys.argv[1],"r")
string=f.read()
#slist=nltk.word_tokenize(string)
slist=string.split()
words=slist
stop = stopwords.words('english')
stop=[x.encode('UTF8') for x in stop]
slist=set(slist)
slist=list(slist)
filtered_words = [w for w in slist if not w.lower() in stop]
frequency=[0]*len(slist)
topwords=[0]*len(slist)
temp=0
for i in filtered_words:
    frequency[temp]=words.count(i)
    topwords[temp]=temp
    temp=temp+1
for i in range( 0,len(frequency) ):
   for k in range(0, len(frequency)-1):
     if ( frequency[k] < frequency[k+1] ):
       temp=frequency[k]
       frequency[k]=frequency[k+1]
       frequency[k+1]=temp
       temp=topwords[k]
       topwords[k]=topwords[k+1]
       topwords[k+1]=temp
print frequency, topwords
for i in range(0,10):
    print filtered_words[topwords[i]]+'\n'

