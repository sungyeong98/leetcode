class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        temp=heights.copy()
        temp.sort(reverse=True)

        result=[]
        for i in temp:
            result.append(names[heights.index(i)])
        return result