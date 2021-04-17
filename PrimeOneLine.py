c=list(map(lambda x:all(x % y!=0 for y in range(2,x)),range(2,13)))
#list(map(int, c)) #converts to 0's and 1's
Primecount=0
for i in c:
  if(i==True):
    Primecount+=1
  else:
    continue
print("Count",Primecount)
