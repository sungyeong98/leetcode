class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        if set(nums1)&set(nums2):
            return min(set(nums1)&set(nums2))
        
        n1,n2=min(nums1),min(nums2)
        return int(str(n1)+str(n2)) if n1<n2 else int(str(n2)+str(n1))