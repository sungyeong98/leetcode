class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        dm = dn = 0
        temp=[]
        
        while dm<len(nums1) and dn<len(nums2):
            if nums1[dm]<nums2[dn]:
                temp.append(nums1[dm])
                dm+=1
            elif nums1[dm]>nums2[dn]:
                temp.append(nums2[dn])
                dn+=1
            elif nums1[dm]==nums2[dn]:
                temp.append(nums1[dm])
                temp.append(nums2[dn])
                dm+=1
                dn+=1
        
        while dm<len(nums1):
            temp.append(nums1[dm])
            dm+=1
        while dn<len(nums2):
            temp.append(nums2[dn])
            dn+=1

        if (m+n)%2==1:
            return temp[(m+n)//2]
        else:
            mid=(m+n)//2
            return (temp[mid]+temp[mid-1])/2