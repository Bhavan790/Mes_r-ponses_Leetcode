class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res=[]
        num=Counter(nums)
        while num :
            tar=[]
            for i in list(num.keys()) :
                tar.append(i)
                num[i]-=1
                if num[i]==0 :
                    del num[i]
            res.append(tar)
        return res