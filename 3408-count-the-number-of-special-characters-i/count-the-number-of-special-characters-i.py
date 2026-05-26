class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        a="abcdefghijklmnopqrstuvwxyz"
        count=0
        for i in a :
            if i.upper() in word and i in word :
                count+=1
        return count