def countingSort(arr):
    m=max(arr)+1
    result=[0]*m
    for i in arr:
        result[i]+=1
    return result 
