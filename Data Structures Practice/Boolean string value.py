for i in range(int(input())):
    s=list(input())
    s=s[::-1]
    while len(s)!=1:
        a,op,b=s.pop(),s.pop(),s.pop()
        if op=="A":
            s.append(int(a) & int(b))
        elif op=="B":
            s.append(int(a) | int(b))
        elif op=="C":
            s.append(int(a) ^ int(b))
    print(s.pop())
