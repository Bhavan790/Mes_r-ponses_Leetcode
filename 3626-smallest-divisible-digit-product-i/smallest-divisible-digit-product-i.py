class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True :
            res=1
            for i in str(n) :
                res*=int(i)
            if res%t==0 :
                return n
            n+=1