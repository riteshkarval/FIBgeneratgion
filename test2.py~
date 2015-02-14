import re
string='Most software engineers would agree that good object oriented designs are inherently more maintainable'
sub1='(.*)'
query=raw_input("query\n").split()
sub=sub1+query[0]+sub1+query[len(query)-1]+sub1
obj=re.search(sub,string,re.I)
if obj:
    print obj.group(2)
