class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        #solution1
        '''
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
                    result.append([max(j[0],i[0]),max(j[1],i[0])])
        return result
        '''

        #solution2
        i,j=0,0
        n,m=len(firstList),len(secondList)
        result=[]
        while i<n and j<m:
            start=max(firstList[i][0],secondList[j][0])
            end=min(firstList[i][1],secondList[j][1])
            if start<=end:
                result.append([start,end])
            if end==firstList[i][1]:
                i+=1
            else:
                j+=1
        return result