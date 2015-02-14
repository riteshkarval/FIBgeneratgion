import nltk
import nltk.data
import sys
from pyPdf import PdfFileReader
import pyPdf
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
p=raw_input("file name or path:  ")
pdf = PdfFileReader(file(p, 'rb'))
content=""
for i in range(1, pdf.getNumPages()):
          content += pdf.getPage(i).extractText() + " \n"
          content = " ".join(content.replace(u"\xa5", u" ").strip().split())
string=str(content)
#print string
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
