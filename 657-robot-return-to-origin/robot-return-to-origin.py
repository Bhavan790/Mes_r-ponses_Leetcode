class Solution:
    def judgeCircle(self, moves: str) -> bool:
        h,v=0,0
        for i in moves :
            if i=='U' :
                v+=1
            elif i=='D' :
                v-=1
            elif i=='R' :
                h+=1
            elif i=='L' :
                h-=1
        return v==0 and h==0