class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        arr.sort()
        n=len(arr)/2
        ou=[1]
        for i in range (1,len(arr)):
            if arr[i] ==arr[i-1]:
                ou[-1]+=1
            else:
                ou+=[1]
        ou.sort()
        ou.reverse()
        fin=0
        for i in range(len(ou)):
            fin+=ou[i]
            if fin>=n:
                break
        return i+1
