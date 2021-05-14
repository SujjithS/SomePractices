import threading

def printSquare(num):
  print("Cube: {}".format(num*num))
def printCube(num):
  print("Square: {}".format(num*num*num))

#create Thread
t1=threading.Thread(target=printSquare,args=(10))
t2=threading.Thread(target=printCube,args=(10))

#start Thread
t1.start()
t2.start()


#wait until t1 is completely executed
t1.join()

#wait until t2 is completely executed
t2.join()

print("Done!")