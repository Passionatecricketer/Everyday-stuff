for i in range(int(input())):
    n = int(input())
    z = bin(n)
    z = str(z).split('b')[1]
    print('0'*(14-len(z))+z)
