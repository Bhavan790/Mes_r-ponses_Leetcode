class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        bucket={}
        for i in range(len(mat)) :
            for j in range(len(mat[0])) :
                s=i-j 
                if s not in bucket :
                    bucket[s]=[]
                bucket[s].append(mat[i][j]) 
        for i in bucket :
            bucket[i].sort(reverse=True)
        for i in range(len(mat)) :
            for j in range(len(mat[0])) :
                mat[i][j]=bucket[i-j].pop()
        return mat