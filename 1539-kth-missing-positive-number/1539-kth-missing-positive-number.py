class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        return bisect_right(range(len(arr)), k, key=lambda x:arr[x]-x)+k