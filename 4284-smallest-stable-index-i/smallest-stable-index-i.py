class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        count,idx=0,0
        for i in range(len(nums)) :
            p=max(nums[:i+1])
            q=min(nums[i:])
            if p-q<=k :
                return i
        return -1