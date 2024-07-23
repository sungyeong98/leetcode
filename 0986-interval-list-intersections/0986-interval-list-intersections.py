class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result=[]
        for i in firstList:
            for j in secondList:
                if i[1]<j[0]:
                    break
                if i[0]>j[1]:
                    continue
                if i[1]<=j[1]:
                    result.append([max(i[0],j[0]),min(i[1],j[1])])
                else:
                    result.append([min(j[1],i[0]),max(j[1],i[0])])
        return result