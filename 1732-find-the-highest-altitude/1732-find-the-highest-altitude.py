class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result=[0]
        for i in gain:
            result.append(result[-1]+i)
        return max(result)