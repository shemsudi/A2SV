class Solution(object):
    def targetIndices(self, nums, target):
        lis=[]
        nums.sort()
        for i in range (len(nums)):
            if nums[i]==target:
                lis+=[i]
        return lis
