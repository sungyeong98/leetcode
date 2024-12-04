class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:
            return sum(nums)

        nums.sort()
        n, result = len(nums), float('inf')

        for idx, val in enumerate(nums):
            next_idx, k = idx + 1, n - 1
            while next_idx < k:
                temp = val + nums[next_idx] + nums[k]
                if temp == target:
                    return temp
                if abs(temp-target) < abs(result - target):
                    result = temp
                if temp > target:
                    k-=1
                else:
                    next_idx += 1
        return result