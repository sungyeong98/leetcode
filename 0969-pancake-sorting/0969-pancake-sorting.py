class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        end=len(arr)
        result=[]
        while end>1:
            max_idx=arr.index(end)
            if max_idx==end-1:
                end-=1
                continue
            if max_idx!=0:
                arr[:max_idx+1]=reversed(arr[:max_idx+1])
                result.append(max_idx+1)
            arr[:end]=reversed(arr[:end])
            result.append(end)
            end-=1
        return result