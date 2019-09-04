t = int(input())
for i in range(t):
    s = input()
    s = s.split(" ")
    n = int(s[0])
    m = int(s[1])
    m = abs(m)
   
    q = n // m
    n1 = m * (q+1)
    n2 = m * (q)

    diff1 = n1 - (n)
    diff2 = (n) - n2
    if diff1 > diff2:
        print(n2)
    elif diff2 > diff1:
        print(n1)
    else:
        if(q>0):
            print(n1)
        else:
            print(n2)
