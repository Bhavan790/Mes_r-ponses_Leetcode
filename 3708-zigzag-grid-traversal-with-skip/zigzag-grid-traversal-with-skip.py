class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res=[]
        m,n=len(grid),len(grid[0])
        for i in range(m) :
            if i%2==0 :
                res.extend(grid[i])
            else :
                res.extend(grid[i][::-1])
        ans=[]
        for i in range(len(res)) :
            if  i%2==0 :
                ans.append(res[i])
        return ans
