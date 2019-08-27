def checkPalindrome(string):
    if(string == string[::-1]):
        print("Yes")
    else:
        print("No")

testcases = int(input()) 
while(testcases):
    len = int(input())
    string = input()
    checkPalindrome(string)
    testcases=testcases-1
