class Solution(object):
    def sortColors(self, nums):
       
        n=len(nums)
        for i in range (1,n):
            v=nums[i]
            p=i
            while p>0 and v<nums[p-1]:
                nums[p]=nums[p-1]
                p=p-1
                print(nums)
            nums[p]=v
            print(nums
