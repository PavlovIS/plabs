text=input()
u=''
wordlist=list()
wtext=text+' '
for i in wtext:
 if i==' ':
  wordlist.append(u)
  u=''
 else:
   u=u+i
maxw=''
maxi=0
for i in wordlist:
 if maxi<wordlist.count(i):
  maxw=i
  maxi=wordlist.count(i)
print(maxw)

input()
