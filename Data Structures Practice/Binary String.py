t=int(input())
for i in range(t):
    n=int(input())
    l=list(input())
    c=0
    res=0
    for i in range(0,n):
        if l[i]=="1":
            c+=1;
    res= int(c*(c-1)/2)
    print(res)
