t=int(input())
for i in range(t):
    a=input()
    b=input()
    s=""
    j=0
    while(j<len(a)):
        if(a[j] in b):
            j+=1
        else:
            s=s+a[j]
            j+=1
    k=0
    while(k<len(b)):
        if(b[k] in a):
            k+=1
        else:
            s=s+b[k]
            k+=1
    if(len(s)>0):
        print(s)
    else:
        print(-1)
