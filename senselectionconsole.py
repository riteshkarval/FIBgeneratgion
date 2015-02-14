import nltk
import nltk.data
import sys
from pyPdf import PdfFileReader
import pyPdf
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
string=raw_input("Enter Text:  ")
slist=sentdec.tokenize(string.strip())
score= [0] *len(slist)
impsen=[0]*len(slist)
for x in range(0,(len(slist))):
    s2list=nltk.word_tokenize(slist[x])
    score[x]=float(len(s2list))/len(set(s2list))
    impsen[x]=x;
#print score
#print len(score)
for i in range( 0,len(score) ):
   for k in range(0, len(score)-1):
     if ( score[k] > score[k+1] ):
       temp=score[k]
       score[k]=score[k+1]
       score[k+1]=temp
       temp=impsen[k]
       impsen[k]=impsen[k+1]
       impsen[k+1]=temp
print "Top 10 sentences in document are: \n"
for i in range(0,10):
    print slist[impsen[i]]+'\n'
       
     
'''
tokens=nltk.word_tokenize(raw)
text=nltk.Text(tokens)
type(text)
text.concordance("players")
text.collocations()
'''
