class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        temp=[arr[i+1]-arr[i] for i in range(len(arr)-1)]
        if len(set(temp))==1:
            return True
        return False