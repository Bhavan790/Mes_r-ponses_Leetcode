class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k :
            res=[]
            a,b=0,0
            for i in s :
                a+=1
                b+=int(i)
                if a==k :
                    res.append(str(b))
                    a,b=0,0
            if a>0 :
                res.append(str(b))
            s="".join(res)
        return s