t = int(input())
while t > 0:
    text = input()
    sp = text.split(".")
    for i in range(len(sp)):
        sp[i]=sp[i][::-1]
    
    #print (sp)
    string = '.'.join(sp) 
    #print (string)
    print(string[::-1])
    t -= 1
