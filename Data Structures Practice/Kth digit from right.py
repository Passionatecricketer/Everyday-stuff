for i in range(int(input())):
    a,b,k = map(int,input().split())
    p = str(a**b)
    rp = p[::-1]
    print (rp[k-1])
