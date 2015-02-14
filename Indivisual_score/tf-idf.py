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
def seq_search(query,string):
    sub1='(.*)'
    sub=sub1
    for i in query.split():
        sub=sub+i+sub1
    #print sub
    obj=re.search(sub,string,re.I)
    if obj:
        return True
    else:
        return False
def substr_len(query,string):
    q=query.split()
    if(len(q)==1):
        return 1
    else:
        sub1='(.*)'
        sub=sub1+q[0]+sub1+q[len(q)-1]+sub1
        obj=re.search(sub,string,re.I)
        return (len(obj.group(2).split())+2)
import nltk
import re
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
#tf-idf value of query words
#print wlist
sum_tf_idf=0
for x in range(0,(len(filtered_query))):
    tf=float(wlist.count(filtered_query[x]))/len(wlist)
    #print wlist.count(filtered_query[x]),len(wlist)
    idf=float(len(slist))/presence_in(filtered_query[x],slist)
    print idf
    #print tf,idf
    tf_idf[x]=tf*idf
    sum_tf_idf=sum_tf_idf+tf_idf[x]
print tf_idf

selectedsen=[]
imp=[]
ld=[]
pos_weight=[]
for x in range(0,(len(slist))):
    tstr=slist[x].lower()
    if slist[x] not in selectedsen:
        if(query in tstr):
            s2list=nltk.word_tokenize(tstr)
            timp=1+sum_tf_idf
        #if slist[x] not in selectedsen:
            selectedsen.append(slist[x])
            imp.append(timp)
        elif(seq_search(query,tstr)):
            s2list=nltk.word_tokenize(tstr)
            #Lq/Lss
            Lq=len(query.split())
            Lss=substr_len(query,slist[x])
            timp=(float(Lq)/Lss)+sum_tf_idf
            #if slist[x] not in selectedsen:
            selectedsen.append(slist[x])
            imp.append(timp)
        else:
            timp=0
            for i in range(0,len(filtered_query)):
                if filtered_query[i] in tstr:
                        timp=timp+tf_idf[i]
            if (timp>0):
                selectedsen.append(slist[x])
                imp.append(timp)

score=[0]*len(selectedsen)
topsen=[0]*len(selectedsen)
for i in range(0,len(selectedsen)):
    topsen[i]=i
    score[i]=imp[i]

for i in range( 0,len(score) ):
   for k in range(0, len(score)-1):
     if ( score[k]<score[k+1] ):
         temp=score[k]
         score[k]=score[k+1]
         score[k+1]=temp                         
         temp=topsen[k]
         topsen[k]=topsen[k+1]
         topsen[k+1]=temp
print len(selectedsen), len(set(selectedsen))
for i in range(0,len(selectedsen)):
    print 'Sentence-',i+1,'\n'
    print '*************************\n'
    print selectedsen[topsen[i]]+'\n'
    print '*************************\n'
    if(i>19):
        break
