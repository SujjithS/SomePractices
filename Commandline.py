import sys
print ("The script has the name")
ran=list(map(int,sys.argv[1:]))
for i in range(ran[0],ran[1]):
    print(i)
