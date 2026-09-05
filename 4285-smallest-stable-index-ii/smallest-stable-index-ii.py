class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        count=0
        l=nums[0]
        p=[]
        for i in nums :
            l=max(l,i)
            p.append(l)
        r=nums[-1]
        s=[]
        for i in reversed(nums) :
            r=min(r,i)
            s.append(r)
        s=s[::-1]
        for i in range(len(nums)) :
            if p[i]-s[i]<=k :
                return i

        return -1