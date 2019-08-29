import calendar
t=int(input())
for i in range(t):
    d,m,y=map(int,input().split())
    s=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    a=calendar.weekday(y,m,d)
    print(s[a])
