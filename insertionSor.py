def insertionSort1(m, arr):
    # Write your code here
    for i in range (1,n):
        v = arr[n - i]
        p=n-i
        while p>0 and v<arr[p - 1]:
            arr[p]=arr[p - 1]
            p=p-1
            for i in range(n):
                if i != n - 1:
                    print(arr[i], end=" ")
                else:
                    print(arr[i])
            
        arr[p]=v
    for i in range(n):
        if i != n - 1:
            print(arr[i], end=" ")
        else:
            print(arr[i])
