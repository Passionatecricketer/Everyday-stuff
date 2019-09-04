t = int(input())
while t>0:
    a=0
    b=1
    print(b,end=' ')
    n= int(input())
    for i in range(1,n):
        c=a + b
        a=b
        b=c
        print(c,end=' ')
    print()
    t=t-1
