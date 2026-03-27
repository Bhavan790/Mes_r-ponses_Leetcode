class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        res=deepcopy(mat)
        # s=0
        k%=len(mat[0])
        for _ in range(k) :
            # print(s)
            for i in range(len(res)) :
                if i%2==0 :
                    res[i].append(res[i].pop(0))
                else :
                    res[i].insert(0,res[i].pop())
            # s+=1
            # print(res)
        return mat==res