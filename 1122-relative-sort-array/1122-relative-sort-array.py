class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[]
        a1=Counter(arr1)
        temp=list(set(arr1))
        temp.sort()
        for n in arr2:
            result+=[n]*a1[n]
        for n in temp:
            if n not in arr2:
                result+=[n]*a1[n]
        return result