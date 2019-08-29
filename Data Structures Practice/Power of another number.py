t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if x == 1:
        print(1 if y == 1 else 0)
        continue
    while y%x == 0:
        y //= x
    print(1 if y == 1 else 0)
