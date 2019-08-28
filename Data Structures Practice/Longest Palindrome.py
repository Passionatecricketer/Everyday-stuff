for i in range(int(input())):
    s = input()
    lst=[]
    for i in range(len(s)):
        for j in range(len(s),i,-1):
            if s[i:j] not in lst:
                lst.append(s[i:j])
    ans = ""
    lst.sort(key = len)
    flag=0
    for i in lst[::-1]:
        if i == i[::-1] and len(i)>1 and len(i)>=len(ans):
           ans = i
    if len(ans)>1:
        flag=1
    if flag==0:
        print(lst[0])
    else:
        print(ans)
