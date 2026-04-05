class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = R = S = 0
        for i in moves :
            if i=='L' :
                L+=1
            elif i=='R' :
                R+=1
            else :
                S+=1
        return S+abs(R-L)