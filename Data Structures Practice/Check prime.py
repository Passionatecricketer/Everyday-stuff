def chkprime(n):
    for i in range(2,n):
	    if (n % i  == 0):
		    return 0
		    break
    else:
        return 1


for i in range(int(input())):
    n = int(input())
    for j in range(2,n//2):
        if chkprime(j) and chkprime(n-j):
            print (j,n-j)
            break
