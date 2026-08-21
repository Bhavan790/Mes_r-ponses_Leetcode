class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums) 
        c=Counter(nums)
        if k==1 :
            ans=-1
            for i,j in c.items() :
                if j==1 and i>ans :
                    ans=i
            return ans
        elif k==n :
            return max(nums)
        ans=-1
        if c[nums[0]]==1 :
            ans=max(ans,nums[0])
        if c[nums[-1]]==1 :
            ans=max(ans,nums[-1])
        return ans