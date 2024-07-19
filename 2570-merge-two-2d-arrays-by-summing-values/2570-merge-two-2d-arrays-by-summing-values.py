class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        temp=defaultdict(int)
        for idx,val in nums1:
            temp[idx]+=val
        for idx,val in nums2:
            temp[idx]+=val
        return list(sorted(temp.items(), key=lambda x:x[0]))