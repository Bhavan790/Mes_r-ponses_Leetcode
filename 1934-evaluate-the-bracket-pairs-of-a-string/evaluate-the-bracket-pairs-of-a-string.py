class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        res={}
        for i in knowledge :
            res[i[0]]=i[1]
        add=0
        ch=""
        ans=""
        for i in s :
            if i==')' :
                ans+=res.get(ch,"?")
                add=0
                ch=""
            elif add==1 :
                ch+=i
            elif i=='(' :
                add=1
            else :
                ans+=i
        return ans