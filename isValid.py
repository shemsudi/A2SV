class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sol=[]
        c=0
        v=0
        t=0

        for i in s:
            if len(s)%2==0:
                if s[0]==")" or s[0]=="]" or s[0]=="}":
                    return False
                    break
                elif len(sol)>0 and (sol[0]==")" or sol[0]=="]" or sol[0]=="}"):
                    return False
                    break
                elif i=="(" or i=="[" or i=="{":
                    sol.append(i)
                    c+=1
                    v+=1
                elif i==")":
                    c+=1
                    t+=1
                    if len(sol)>0 and sol.pop()!="(":
                        return False
                        break
                elif i=="]":
                    c+=1
                    t+=1
                    if len(sol)>0 and sol.pop()!="[":
                        return False
                        break
                elif i=="}":
                    c+=1
                    t+=1
                    if len(sol)==0:
                        return False
                    elif len(sol)>0 and sol.pop()!="{":
                        return False
                        break
            else:
                return False
        if c==len(s) and v==t:
            return True
        if c==len(s) and v!=t:
            return False
