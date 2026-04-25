class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        if len(set(colors)) == 1:
            return 0
        n=len(colors)
        l,r=0,n-1
        for i in range(n) :
            if colors[i]!=colors[-1] :
                l=i
                break
        for i in range(n-1,-1,-1) :
            if colors[i]!=colors[0] :
                r=i
                break
        return max(n-1-l,r)