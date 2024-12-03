class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prevMax, curMin, curMax = 0, 0, 0
        prevBit = -1

        for i in nums:
            temp = i.bit_count()
            if prevBit!=temp:
                if curMin<prevMax:
                    return False
                prevMax=curMax
                curMin, curMax = i, i
                prevBit = temp
            else:
                curMin = min(curMin, i)
                curMax = max(curMax, i)
        return curMin>=prevMax