class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums :
            a=str(i)
            for j in a :
                res.append(int(j))
        return res
            