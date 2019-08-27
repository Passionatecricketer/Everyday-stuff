t = int(input())
while t > 0:
    s = input()
    vowels = []
    for i in s:
        if i in "aeiou":
            vowels.append(i)
    new = ""
    for i in s:
        if i in "aeiou":
            new += vowels.pop()
        else:
            new += i
    print(new)
    t -= 1
