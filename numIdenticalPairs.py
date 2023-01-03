class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=[]
        for i in range(len(nums)):
            for j in range (len(nums)):
                if nums[j]==nums[i] and i<j:
                    num+=[[j,i]]
        
        return len(num)
