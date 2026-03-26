class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        n=numRows
        p=len(s)
        res = [['' for _ in range(p)] for _ in range(n)]
        x,y=0,0
        flag=0
        for i in range(p) :
            res[x][y]=s[i]
            if flag==0:
                if x==n-1 :
                    flag=1
                    x-=1
                    y+=1
                else :
                    x+=1
            else :
                if x==0 :
                    flag=0
                    x+=1
                else :
                    x-=1
                    y+=1
        fin=''
        for i in res :
            fin+=''.join(i)
        return fin