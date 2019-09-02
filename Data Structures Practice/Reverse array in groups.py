for i in range(int(input())):
    n,g = map(int,input().split())
    l = list(map(int,input().split()))
    for i in range(0,n,g):
        newl = l[i:i+g]
        newl.reverse()
        for k in range(len(newl)):
            print (newl[k],end = " ")
    print()
