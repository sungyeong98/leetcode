class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1,n2=set(nums1),set(nums2)
        result=n1&n2
        return min(result) if result else -1