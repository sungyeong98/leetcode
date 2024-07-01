class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return sum(nums2)/len(nums2)
        if not nums2:
            return sum(nums1)/len(nums1)
        
        n1=sum(nums1)/len(nums1)
        n2=sum(nums2)/len(nums2)
        return (n1+n2)/2