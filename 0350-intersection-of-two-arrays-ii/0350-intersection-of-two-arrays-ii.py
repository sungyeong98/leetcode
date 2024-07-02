import copy
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for num in nums2:
            if num in nums1:
                nums1.remove(num)
                result.append(num)
        return result