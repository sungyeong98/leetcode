class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c=Counter(arr)
        n=len(arr)
        return sorted(c.items(), key=lambda x:-x[1])[0][0]