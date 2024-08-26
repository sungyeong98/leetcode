class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        idx=defaultdict(list)
        left, right = 0, nums.count(1)
        idx[left+right].append(0)
        for i in range(1, len(nums)+1):
            if nums[i-1]==0:
                left+=1
            else:
                right-=1
            idx[left+right].append(i)
        return idx[max(idx.keys())]