import sys
import time
def my_Prime(n):
  if(n<=1): #no prime number before 2
    return False
  for i in range(2,n):
    if(n%i==0):
      return False
  else:
    return True

t0=time.time()
c=0
r=list(map(int,sys.argv[1:]))
for n in range(r[0],r[1]):
  x=my_Prime(n)
  c+=x
print("total prime numbers are: ",c)
t1=time.time()
print("Total time consumed: ",t1-t0)
