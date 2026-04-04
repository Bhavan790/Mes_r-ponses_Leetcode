class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res=[]
        row,col=0,0
        m,n=len(mat),len(mat[0])
        up=True
        while len(res) < m*n :
            res.append(mat[row][col])
            if up :
                if col==n-1 :
                    row+=1
                    up=False
                elif row==0 :
                    col+=1
                    up=False
                else :
                    row-=1
                    col+=1
            else :
                if row==m-1 :
                    col+=1
                    up=True
                elif col==0 :
                    row+=1
                    up=True
                else :
                    row+=1
                    col-=1 
        return res