class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        nums=defaultdict(list)

        for a,b,c in triplets:
            nums[0].append(a)
            nums[1].append(b)
            nums[2].append(c)

        for idx, val in enumerate(target):
            if min(nums[idx])>val or val not in nums[idx]:
                return False
            elif min(nums[idx])==val and len(nums[idx])>=2 and nums[idx].count(val)==1:
                return False
        
        return True