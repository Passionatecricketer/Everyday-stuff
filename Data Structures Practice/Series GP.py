import math
for i in range(int(input())):
    a,b = map(int,input().split())
    n = int(input())
    cr = b/a
    print (math.floor(a*(cr**(n-1))))
