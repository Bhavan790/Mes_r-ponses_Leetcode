class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n=len(words)
        s={}
        for i in words :
            for j in range(len(i)) :
                if i[j] in s :
                    s[i[j]]+=1
                else :
                    s[i[j]]=1
        for i,j in s.items() :
            if j%n!=0 :
                return False
        return True