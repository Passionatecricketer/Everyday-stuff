t = int(input())
while(t>0):
    a = list(map(int, input().split()))
    a.sort()
    b = set()
    for i in range(len(a)):
        b.add(a[i])
    if(len(b) == 2):
        print(1)
    else:
        print(0)
    t=t-1
