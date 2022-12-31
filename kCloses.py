class Solution(object):
    def kClosest(self, points, k):
        import math
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dl=[]
        dm=[]
        df=[]
        for i in points:
           d= (i[0]**2+i[1]**2)
           dl+=[d]
           dm+=[d]
        dm.sort()
        dm=dm[:k]
   

        for i in dm:
            df+=[points[dl.index(i)]]
            dl[dl.index(i)]="u"
        return df
