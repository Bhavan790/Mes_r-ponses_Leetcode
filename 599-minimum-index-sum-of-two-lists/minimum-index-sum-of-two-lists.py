class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        min_num=float('inf')
        for i in range(len(list1)) :
            for j in range(len(list2)) :
                if list1[i]==list2[j] and list1[i] not in res :
                    if i+j<min_num :
                        min_num=i+j
                    res.append((list1[i],i+j))
        ans=[]
        for i,j in res :
            if j==min_num :
                ans.append(i)
        return ans