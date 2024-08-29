class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        keys, result = {}, []
        for i in pieces:
            keys[i[0]]=i
        for i in arr:
            if i in keys:
                result.extend(keys[i])
        return arr==result