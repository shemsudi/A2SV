class Solution(object):
    def merge(self, inter):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n= len(inter) - 1
        fin=[]
        inter.sort(key=lambda x: x[0])
        t = [inter[0]]
        for i in range (n):
            if inter[i+1][1]>t[0][1] and inter[i+1][0]>t[0][0] and inter[i+1][0]!=t[0][1] and t[0][1]<inter[i+1][0]:
                fin+=t
                t=[inter[i+1]]
            else:
                t=[[min(t[0][0],inter[i+1][0]),max(t[0][1],inter[i+1][1])]]
        fin+=t
          
        return fin
