for i in range(int(input())):
    n= int(input())
    l = list(map(int,input().split()))
    newl = l[::-1]
    for i in range(len(newl)):
        print (newl[i],end = " ")
    print ()
