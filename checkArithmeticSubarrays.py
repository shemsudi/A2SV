class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        
        ans=[]
        for i in range (len(r)):
            m=nums[l[i]:r[i]+1]
            m.sort()
            dif = m[1] - m[0]
            c=0
            for j in range (len(m)-1):
                if (m[j+1] - m[j]) != dif:
                    ans.append(False)
                    break
                else:
                    c+=1
            if len(m)-1==c:
                ans.append(True)
