class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<=2 :
            return len(nums)
        a,b=min(nums),max(nums)
        l,r=0,len(nums)-1
        i,j=0,0
        p,q=0,0
        while nums[l]!=a and nums[l]!=b :
            i+=1
            l+=1
        i+=1
        while nums[r]!=a and nums[r]!=b :
            j+=1
            r-=1
        j+=1
        k,s=0,2
        while s>0 :
            if nums[k]==a or nums[k]==b :
                s-=1
            p+=1
            k+=1
        k,s=len(nums)-1,2
        while s>0 :
            if nums[k]==a or nums[k]==b :
                s-=1
            q+=1
            k-=1
        return min(p,q,(i+j))