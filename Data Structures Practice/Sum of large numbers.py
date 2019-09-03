for i in range(int(input())):
    x,y = map(int,input().split())
    sum = x+y
    
    if len(str(x))==len(str(sum)):
        print (sum)
    else:
        print (x)
