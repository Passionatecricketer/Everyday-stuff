for i in range(int(input())):
    n = int(input())
    z = bin(n)
    try:
        index=z[::-1].index('1')
        print(index+1)
    except:
        print(0)
