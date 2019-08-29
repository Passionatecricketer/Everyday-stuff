t=int(input())
for _ in range(t):
    n=int(input())
    if n==0:
        print('NO')
    else:

        if n&(n-1)==0:
            print('YES')
        else:
            print('NO')
