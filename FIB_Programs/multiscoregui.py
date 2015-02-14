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

def difficulty(sentence,query,Do):
    No=sentence.count(query)
    Lq=len(query.split())
    sen=sentence.split()
    stop = stopwords.words('english')
    stop=[x.encode('UTF8') for x in stop]
    #Ls=len([w for w in sen if not w in stop])
    Ls=len(sen)
    '''
    print Ls,Lq,No
    Dscore=(1.0/(No*frac))+(1.0/(Ls-No*Lq))-1.0
    '''
    Dscore=(1.0/100)*((50.0/No)+(20.0/Ls)+(30.0/Do))
    print Dscore,No,Ls,Lq,Do
    if(Dscore>=0.55):
        return 'Hard'
    elif(Dscore<0.55 and Dscore>0.30):
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
stop = stopwords.words('english')
stop=[x.encode('UTF8') for x in stop]
f = open(sys.argv[1],"r")
string=f.read().decode('utf-8','ignore')
wlist=string.lower().split()
slist=sentdec.tokenize(string.strip())
queries=(raw_input("Enter query: ")).lower().split(",")
root = Tk()
S = Scrollbar(root)
T = Text(root, height=50,width=70)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
for query in queries:
    query_words=query.split()
    filtered_query = [w for w in query_words if not w in stop]
    selectedsen=[]
    imp=[]
    ld=[]
    pos_weight=[]
    tf_idf=[0]*len(filtered_query)
    sum_tf_idf=0
    #tf-idf of query
    for x in range(0,(len(filtered_query))):
        tf=float(wlist.count(filtered_query[x]))/len(wlist)
        idf=float(len(slist))/presence_in(filtered_query[x],slist)
        tf_idf[x]=tf*idf
        sum_tf_idf=sum_tf_idf+tf_idf[x]
        #selecting sentences from each file
    for x in range(0,(len(slist))):
        tstr=slist[x].lower()
        timp=0
        ls=len(slist[x].split())
        lq=len(query.split())
        if (slist[x] not in selectedsen) and (ls>lq):
            if(query in tstr):
                s2list=nltk.word_tokenize(tstr)
                timp=1+sum_tf_idf
            #if slist[x] not in selectedsen:
                selectedsen.append(slist[x])
                imp.append(timp)
                ld.append(float(len(set(s2list)))/len(s2list))
                index=x+1
                pos_weight.append(1.0/index)
            elif(seq_search(query,tstr)):
                s2list=nltk.word_tokenize(tstr)
                #Lq/Lss
                Lq=len(query.split())
                Lss=substr_len(query,slist[x])
                timp=(float(Lq)/Lss)+sum_tf_idf
            #if slist[x] not in selectedsen:
                selectedsen.append(slist[x])
                imp.append(timp)
                ld.append(float(len(set(s2list)))/len(s2list))
                index=x+1
                pos_weight.append(1.0/index)
            else:
                s2list=nltk.word_tokenize(tstr)
                timp=0
                for i in range(0,len(filtered_query)):
                    if filtered_query[i] in tstr:
                        timp=timp+tf_idf[i]
                if (timp>0):
                    selectedsen.append(slist[x])
                    imp.append(timp)
                    ld.append(float(len(set(s2list)))/len(s2list))
                    index=x+1
                    pos_weight.append(1.0/index)
    score=[0]*len(selectedsen)
    topsen=[0]*len(selectedsen)
    #score calculation
    for i in range(0,len(selectedsen)):
        topsen[i]=i
        #score[i]=(1/len(selectedsen[i]).split())
        score[i]=imp[i]+ld[i]+(1.0/len(selectedsen[i].split()))+pos_weight[i]
        #print imp[i],ld[i],(1.0/len(selectedsen[i])),pos_weight[i]
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
        for i in range(0,len(selectedsen)):
            frac=1
            #print 'Fill in the blank ',i+1,'\n'
            T.insert(END,'Fill in the blank '+str(i+1))
            T.insert(END,'\n')
            T.insert(END,'*************************\n')
            #print '*************************\n'
            if query in selectedsen[topsen[i]].lower():
                if (query[0].title()+query[1:]) in selectedsen[topsen[i]]:
                    T.insert(END,'1-'+selectedsen[topsen[i]].replace(query[0].title()+query[1:],"_______",1))
                    T.insert(END,'\n')
                    T.insert(END,difficulty(selectedsen[topsen[i]].lower(),query,string.lower().count(query)))
                    T.insert(END,'\n')
                else:
                    T.insert(END,'1-'+selectedsen[topsen[i]].replace(query,"_______",1))
                    T.insert(END,'\n')
                    T.insert(END,difficulty(selectedsen[topsen[i]].lower(),query,string.lower().count(query)))
                    T.insert(END,'\n')
                if(len(filtered_query)>1):
                    frac=len(filtered_query)
            if len(filtered_query)>1:
                for j in range(0,len(filtered_query)):
                    if filtered_query[j].title() in selectedsen[topsen[i]]:
                        #print j+1,'-',selectedsen[topsen[i]].replace(filtered_query[j].title(),"____",1)+'\n'
                        T.insert(END, str(j+2)+'-'+selectedsen[topsen[i]].replace(filtered_query[j].title(),"____",1))
                        T.insert(END,'\n')
                        T.insert(END,difficulty(selectedsen[topsen[i]].lower(),filtered_query[j],string.lower().count(filtered_query[j])))
                        T.insert(END,'\n')
                    elif filtered_query[j] in selectedsen[topsen[i]]:
                        #print j+1,'-',selectedsen[topsen[i]].replace(filtered_query[j],"____",1)+'\n'
                        T.insert(END, str(j+2)+'-'+selectedsen[topsen[i]].replace(filtered_query[j],"____",1))
                        T.insert(END,'\n')
                        T.insert(END,difficulty(selectedsen[topsen[i]].lower(),filtered_query[j],string.lower().count(filtered_query[j])))
                        T.insert(END,'\n')
            #print '*************************\n'
            T.insert(END,'*************************\n')
            if(i>3):
                break
    else:
        #pass
        print "No sentence found for ",query,"\n"
mainloop(  )
