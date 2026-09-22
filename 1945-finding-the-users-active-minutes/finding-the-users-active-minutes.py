class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        tar={}
        for i,j in logs :
            if i not in tar :
                tar[i]=[]
            if j not in tar[i] :
                tar[i].append(j)
        res=[0]*k
        for i in tar :
            s=len(tar[i])
            res[s-1]+=1
        return res