def pytago(a,n):
    dict = {}
    for x in a:
        dict[x*x] = 1

    for i in range (n-1):
        for j in range(i+1,n):
            if (a[i]*a[i]+a[j]*a[j]) in dict:
                return 'Yes'
    return 'No'

T = int(input())
for _ in range(T):
    n = int(input())    
    a = list(map(int,input().split()))
    print(pytago(a,n))
