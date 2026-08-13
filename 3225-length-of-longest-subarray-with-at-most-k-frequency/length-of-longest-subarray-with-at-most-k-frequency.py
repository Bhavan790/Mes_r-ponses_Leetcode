class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        a=Counter()
        l,ml=0,0
        for i in range(len(nums)) :
            a[nums[i]]+=1
            while a[nums[i]]>k :
                a[nums[l]]-=1
                l+=1
            ml=max(ml,i+1-l)
        return ml