for i in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    eve=[]
    od=[]
    final=[]
    for i in range(n):
        if (l[i]%2 == 0):
            eve.append(l[i])
        else:
            od.append(l[i])
    eve.sort()
    od.sort()
    od.reverse()
    for i in range(len(od)):
        final.append(od[i])
    for i in range(len(eve)):
        final.append(eve[i])
        
    for i in range(len(final)):
        print (final[i],end = " ")
    print ()
