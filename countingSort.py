def countingSort(arr):
    result=[0]*len(arr)
    for i in arr:
        result[i]+=1
    return result 
