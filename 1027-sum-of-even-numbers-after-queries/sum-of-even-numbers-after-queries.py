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
'start even sum = 6'
'Q1: nums[0]=1 → 2, add 2 → sum=8'
'Q2: nums[1]=2 → -1, remove 2 → sum=6'
'Q3: nums[0]=2 → -2, remove 2 add -2 → sum=2'
'Q4: nums[3]=4 → 6, remove 4 add 6 → sum=4'
'output = [8, 6, 2, 4]'