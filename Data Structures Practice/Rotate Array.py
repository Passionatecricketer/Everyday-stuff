t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    d = int(input())
    print (*(l[d%n:]+l[:d%n]))
