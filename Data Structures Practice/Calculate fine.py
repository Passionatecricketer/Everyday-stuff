for i in range(int(input())):
    n,d = map(int,input().split())
    c = list(map(int,input().split()))
    p = list(map(int,input().split()))
    sum = 0
    if (d%2 == 0):
        for i in range(n):
            if ((c[i]%2)!=0):
                sum += p[i]
        print (sum)
    else:
        for i in range(n):
            if ((c[i]%2)==0):
                sum += p[i]
        print (sum)
    #print ()
