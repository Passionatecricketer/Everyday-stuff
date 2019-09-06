for i in range(int(input())):
    n,s = map(int,input().split())
    l = list(map(int,input().split()))
    suma = 0
    start = 0
    end = 0
    flag = 0
    for j in range(n):
        suma+=l[j]
        end+=1
        if suma>s:
            while suma>s:
                suma = suma-l[start]
                start+=1
        if suma==s:
            flag =1
            break
    if flag==1:
        print (start+1, end)
    else:
        print (-1)
