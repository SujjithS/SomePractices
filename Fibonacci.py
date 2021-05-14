def fibo(n):
    n0=1
    n1=1
    f=0
    if(n==1):
     print(n0)
    elif(n<1):
        return 0
    else:
        print(n0, n1, end=' ')
        for i in range(2,n):
                    f=n0+n1
                    n0=n1
                    n1=f
                    print(f,end=' ')

if __name__=="__main__":
    fibo(10)

