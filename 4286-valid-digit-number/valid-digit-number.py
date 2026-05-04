class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        a,b=str(n),str(x)
        return True if a[0]!=b and b in a else False