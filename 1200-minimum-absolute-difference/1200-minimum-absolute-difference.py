class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff=arr[1]-arr[0]
        result=[]
        for i in range(len(arr)-1):
            n1,n2=arr[i],arr[i+1]
            if n2-n1==diff:
                result.append([n1,n2])
        return result