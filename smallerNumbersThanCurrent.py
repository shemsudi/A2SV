class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        final=[]
        m=len(nums)
        for i in range(m) :
            count=0
            for j in range(m) :
                if nums[j] < nums[i]:
                    count+=1
            final.append(count)
        return final
