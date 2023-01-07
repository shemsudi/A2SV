class Solution(object):
    def topKFrequent(self, arr, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        ou=[[1,0]]
        for i in range (1,len(arr)):
            if arr[i] ==arr[i-1]:
                ou[-1][0]+=1
            else:
                ou+=[[1,i]]
        ou.sort()
        ou.reverse()
        fin=[]
        for i in range (k):
           fin+=[arr[ ou[i][-1]]]
        return fin
