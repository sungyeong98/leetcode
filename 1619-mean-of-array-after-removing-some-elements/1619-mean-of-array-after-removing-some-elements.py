class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n=len(arr)
        t=int(n*0.05)

        return sum(arr[t:-t])/len(arr[t:-t])