class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        n=len(nums)
        num=[]
        for i in range (n):
            num+=[int(nums[i])]
        num.sort()
        return str(num[-1*k])
