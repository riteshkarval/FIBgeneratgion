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
def difficulty(sentence,query,frac):
    No=sentence.count(query)
    Ls=len(sentence.split())
    Lq=len(query.split())
    Dscore=(1.0/(No*frac))+(1.0/(Ls-No*Lq))-1.0
    print Dscore,No,Ls,Lq
    if(Dscore<=1.0 and Dscore>=0.07):
        return 'Hard'
    elif(Dscore<=0.07 and Dscore>=0.05):
        return 'Medium'
    else:
        return 'Low'
    
import nltk
import re
import nltk.data
import sys
from Tkinter import *
from nltk.corpus import stopwords
sentdec=nltk.data.load('tokenizers/punkt/english.pickle')
f = open(sys.argv[1],"r")
string=f.read().decode('utf-8','ignore')
#wlist=nltk.word_tokenize(string.lower())
slist=sentdec.tokenize(string.strip())
stop = stopwords.words('english')
stop=[x.encode('UTF8') for x in stop]
query=(raw_input("Enter query: ")).lower().split(",")
root = Tk()
S = Scrollbar(root)
T = Text(root, height=50,width=70)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
for q in query:
    query_words=q.split()
    filtered_query = [w for w in query_words if not w in stop]
    selectedsen=[]
    imp=[]
    ld=[]
    for x in range(0,(len(slist))):
        tstr=slist[x].lower()
        timp=0
        if slist[x] not in selectedsen:
            if(q in tstr):
                s2list=nltk.word_tokenize(tstr)
                timp=1
            #if slist[x] not in selectedsen:
                selectedsen.append(slist[x])
                imp.append(timp)
                ld.append(float(len(set(s2list)))/len(s2list))
            elif(seq_search(q,tstr)):
                s2list=nltk.word_tokenize(tstr)
                #Lq/Lss
                Lq=len(q.split())
                Lss=substr_len(q,slist[x])
                timp=(float(Lq)/Lss)
                #if slist[x] not in selectedsen:
                selectedsen.append(slist[x])
                imp.append(timp)
                ld.append(float(len(set(s2list)))/len(s2list))
            else:
                s2list=nltk.word_tokenize(tstr)
                timp=0
                for i in range(0,len(filtered_query)):
                   if filtered_query[i] in tstr:
                            timp=1
                if (timp>0):
                    selectedsen.append(slist[x])
                    imp.append(0)
                    ld.append(float(len(set(s2list)))/len(s2list))
    score=[0]*len(selectedsen)
    topsen=[0]*len(selectedsen)
    for i in range(0,len(selectedsen)):
        topsen[i]=i
        score[i]=imp[i]+ld[i]

    for i in range( 0,len(score) ):
       for k in range(0, len(score)-1):
         if ( score[k]<score[k+1] ):
             temp=score[k]
             score[k]=score[k+1]
             score[k+1]=temp                         
             temp=topsen[k]
             topsen[k]=topsen[k+1]
             topsen[k+1]=temp
    if len(selectedsen)>0:
        #print "Sentences for query-",q,"\n"
        for i in range(0,len(selectedsen)):
            frac=1
            #print 'Fill in the blank ',i+1,'\n'
            T.insert(END,'Fill in the blank '+str(i+1))
            T.insert(END,'\n')
            T.insert(END,'*************************\n')
            #print '*************************\n'
            if q in selectedsen[topsen[i]].lower():
                if q.title() in selectedsen[topsen[i]]:
                    T.insert(END,'1-'+selectedsen[topsen[i]].replace(q.title(),"_______",1))
                    T.insert(END,'\n')
                    T.insert(END,difficulty(selectedsen[topsen[i]].lower(),q,1))
                    T.insert(END,'\n')
                else:
                    T.insert(END,'1-'+selectedsen[topsen[i]].replace(q,"_______",1))
                    T.insert(END,'\n')
                    T.insert(END,difficulty(selectedsen[topsen[i]].lower(),q,1))
                    T.insert(END,'\n')
                if(len(filtered_query)>1):
                    frac=len(filtered_query)
            if len(filtered_query)>1:
                for j in range(0,len(filtered_query)):
                    if filtered_query[j].title() in selectedsen[topsen[i]]:
                        #print j+1,'-',selectedsen[topsen[i]].replace(filtered_query[j].title(),"____",1)+'\n'
                        T.insert(END, str(j+2)+'-'+selectedsen[topsen[i]].replace(filtered_query[j].title(),"____",1))
                        T.insert(END,'\n')
                        T.insert(END,difficulty(selectedsen[topsen[i]].lower(),filtered_query[j],frac))
                        T.insert(END,'\n')
                    elif filtered_query[j] in selectedsen[topsen[i]]:
                        #print j+1,'-',selectedsen[topsen[i]].replace(filtered_query[j],"____",1)+'\n'
                        T.insert(END, str(j+2)+'-'+selectedsen[topsen[i]].replace(filtered_query[j],"____",1))
                        T.insert(END,'\n')
                        T.insert(END,difficulty(selectedsen[topsen[i]].lower(),filtered_query[j],frac))
                        T.insert(END,'\n')
            #print '*************************\n'
            T.insert(END,'*************************\n')
            if(i>3):
                break
    else:
        pass
        #print "No sentence found for ",q,"\n"
mainloop(  )
