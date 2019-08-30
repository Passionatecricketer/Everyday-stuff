t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            print(arr[j+1],end=" ")
        else:
            print("-1",end=" ")

    print("-1")
