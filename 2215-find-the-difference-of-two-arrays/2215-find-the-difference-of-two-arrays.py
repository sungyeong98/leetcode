class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [[i for i in set(nums1)-set(nums2)],[i for i in set(nums2)-set(nums1)]]