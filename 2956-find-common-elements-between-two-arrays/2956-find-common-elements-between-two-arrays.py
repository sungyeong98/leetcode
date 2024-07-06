class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[0, 0]
        for n1 in nums1:
            if n1 in nums2:
                result[0]+=1
        for n2 in nums2:
            if n2 in nums1:
                result[1]+=1
        return result