
class Solution: 
    def select(self, arr, i):
        # code here
        while i<len(arr):
            return i
            i+=1
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
        	sm=i
        	for j in range(i+1,n):
        		if arr[j] <arr[sm]:
        			sm=j
        	if sm!=i:
        		arr[i],arr[sm]=arr[sm],arr[i]
