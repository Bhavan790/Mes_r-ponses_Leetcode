class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ans=[]
        for i in boxGrid :
            for k in range(len(i)) :
                if i[k]=='#' :
                    i[k]=1
                elif i[k]=='.' :
                    i[k]=0
            l=0
            res=[]
            for j in range(len(i)) :
                if i[j]=='*' :
                    seg=sorted(i[l:j])
                    res.extend(seg)
                    res.append('*')
                    l=j+1
            seg=sorted(i[l:])
            res.extend(seg)
            ans.append(res)
        n,m=len(ans),len(ans[0])
        rbox=[[0]*n for _ in range(m)]
        for i in range(n) :
            for j in range(m) :
                rbox[j][n-1-i]=ans[i][j]
        for i in range(m):
            for j in range(n):
                if rbox[i][j]==0:
                    rbox[i][j]='.'
                elif rbox[i][j]== 1:
                    rbox[i][j]='#'
        return rbox