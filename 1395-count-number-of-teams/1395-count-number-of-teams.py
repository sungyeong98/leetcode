class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=0
        for i in combinations(rating, 3):
            temp=list(i)
            if temp[0]>temp[1]>temp[2] or temp[0]<temp[1]<temp[2]:
                result+=1
        return result