#Q2 Sort Florida voters list in ascending order of Democrat voters

import re
fp = open('FloridaVoters.html','r')
line=fp.read()
li=[]

match=re.findall('([a-zA-Z]+[\.\-\sA-Z]*)</td>\n<td>([\d,]+)</td>\n<td>([\d,]+)',line)

#Insertion of each record in it's own list
for rec in match:
    a=list(rec) 
    li.append(a)
    
#print len(li)

#Extract each record from final list and reolace commas with blank chars
for i in li:
    i[1]=i[1].replace(',','')
    i[2]=i[2].replace(',','')
    
li.sort(key=lambda i:float(i[2]))

for i in li:
    print(i[0]+" "+i[1]+" "+i[2]) 