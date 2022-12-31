class Solution(object):
    def sortSentence(self, s):
    
        temp=s.split()
        lis=s.split()
        she=s.split()
        for i in range (0,len(temp)):
            ind= int(temp [i][-1])
            she[ind-1]=temp[i]
        final=""
        for i in she:
            final+=i[:-1] +" "
        return final[:-1]
