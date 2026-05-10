class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s=0
        for i in nums :
            if i%2==0 :
                s+=i
        res=[]
        for i,j in queries :
            old=nums[j]
            new=old+i
            if old%2==0 :
                s-=old
            nums[j]=new
            if new%2==0 :
                s+=new
            res.append(s)
        return res