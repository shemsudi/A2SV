class Solution(object):
    def fizzBuzz(self, n):
        ou=[]
        for i in range (1,n+1):
             ou+=str(i)
    
        for i in range (1,n+1):
            if (i%15)==0:
                ou[i-1]="FizzBuzz"
            elif i%3==0:
                ou[i-1]="Fizz"
            elif i%5==0:
                ou[i-1]="Buzz"
            else:
                ou[i-1]=str(i)
        return ou[:n]
