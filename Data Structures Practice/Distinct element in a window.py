def countDistinct(arr, n, k):
    # Code here
    for i in range(n-k+1):
        print (len(set(arr[i:i+k])),end = " ")
    print ()
