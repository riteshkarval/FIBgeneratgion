def presence_in(word,slist):
    count=0
    for string in slist:
        string=string.lower()
        if(string.count(word)>0):
            count=count+1
    if (count==0):
        return -1
    else:
        return count

import nltk
import nltk.data
import sys
from nltk.corpus import stopwords
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
f = open(sys.argv[1],"r")
string=f.read().decode('utf-8','ignore')
wlist=string.lower().split()
#wlist=nltk.word_tokenize(string.lower())
slist=sentdec.tokenize(string.strip())
stop = stopwords.words('english')
stop=[x.encode('UTF8') for x in stop]
query=(raw_input("Enter query: ")).lower()
query_words=query.split()
filtered_query = [w for w in query_words if not w in stop]
tf_idf=[0]*len(filtered_query)
topwords=[0]*len(filtered_query)
#tf-idf value of query words
#print wlist
for x in range(0,(len(filtered_query))):
    tf=float(wlist.count(filtered_query[x]))/len(wlist)
    #print wlist.count(filtered_query[x]),len(wlist)
    idf=float(len(slist))/presence_in(filtered_query[x],slist)
    #print tf,idf
    tf_idf[x]=tf*idf
    topwords[x]=x
print tf_idf
#sorting query words
for i in range( 0,len(tf_idf) ):
   for k in range(0, len(tf_idf)-1):
     if ( tf_idf[k] < tf_idf[k+1] ):
       temp=tf_idf[k]
       tf_idf[k]=tf_idf[k+1]
       tf_idf[k+1]=temp
       temp=topwords[k]
       topwords[k]=topwords[k+1]
       topwords[k+1]=temp
#scoring sentences
ld=[0]*len(slist)
imp=[0]*len(slist)
topsen=[0]*len(slist)
for x in range(0,(len(slist))):
    tstr=slist[x].lower()
    s2list=nltk.word_tokenize(tstr)
    ld[x]=float(len(set(s2list)))/len(s2list)
    for i in range(0,len(filtered_query)):
        if(s2list.count(filtered_query[topwords[i]])>0):
            imp[x]=imp[x]+tf_idf[i]
        if(i>2):
            break
    topsen[x]=x
#sorting sentences
#print imp,ld
for i in range( 0,len(ld) ):
   for k in range(0, len(ld)-1):
     if ( imp[k]<=imp[k+1] ):
        if(imp[k]==imp[k+1]):
           if(ld[k]<=ld[k+1]):
               if(ld[k]==ld[k+1]):
                   pass
               else:
                   temp=imp[k]
                   imp[k]=imp[k+1]
                   imp[k+1]=temp
                   temp=ld[k]
                   ld[k]=ld[k+1]
                   ld[k+1]=temp                         
                   temp=topsen[k]
                   topsen[k]=topsen[k+1]
                   topsen[k+1]=temp
        else:
            temp=imp[k]
            imp[k]=imp[k+1]
            imp[k+1]=temp
            temp=ld[k]
            ld[k]=ld[k+1]
            ld[k+1]=temp                         
            temp=topsen[k]
            topsen[k]=topsen[k+1]
            topsen[k+1]=temp
for i in range(0,len(filtered_query)):
    print filtered_query[topwords[i]],"\n"
for i in range(0,len(slist)):
    print slist[topsen[i]]+'\n'
    if(i>9):
        break
