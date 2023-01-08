class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ou=[]
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]),len(nums2)):
                if nums1[i]<nums2[j]:
                    ou+=[nums2[j]]
                    break
            if len(ou)<i+1:
                ou+=[-1]
        return ou
