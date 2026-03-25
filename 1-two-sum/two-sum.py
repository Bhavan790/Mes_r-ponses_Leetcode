class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n^2)
        # Space: O(1)
        # Notes: Using nested loops to check every possible pair.
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]