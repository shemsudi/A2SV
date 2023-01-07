class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        n = len(nums)
        j = 0;
        ans = 0;
        for i in range (n):
            k += nums[i]

            while(k < nums[i] * (i - j + 1)):
                k -= nums[j]
                j+=1
            
            ans = max(ans, i - j + 1)
        
        return ans
