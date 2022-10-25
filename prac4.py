##for a given string say abbbccccdddddd
#Expected o/p:ab3c4d6
from collections import Counter
str1=input()
count1=Counter(str1)
for x,y in count1.items():
  if y==1:
    print(x,end="")
  else:
    print(x,y,sep="",end="")

################################
#Method2
str1=input()
d={}
for i in str1:
  if i in d:
    d[i]=d[i]+1
  else:
    d[i]=1

print(d)
for x,y in d.items():
  print(x,y,sep="",end="")
