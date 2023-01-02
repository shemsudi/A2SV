def countSwaps(a):
    
    # Write your code here
    l=len(a)
    c=0
    for i in range (l):
        for j in range(l-1):
            if a[j] >a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                c+=1
    print("Array is sorted in " + str(c) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
