class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result=[]
        if len(arr)==1: return [-1]
        max_num=max(arr[1:])
        for idx,val in enumerate(arr):
            if max_num!=val:
                result.append(max_num)
            else:
                if arr[idx+1:]:
                    max_num=max(arr[idx+1:])
                else:
                    max_num=-1
                result.append(max_num)
        return result