for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    k = int(input())
    l.sort()
    print (l[k-1])
