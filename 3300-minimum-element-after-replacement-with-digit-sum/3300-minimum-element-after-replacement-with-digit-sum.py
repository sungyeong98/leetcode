class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = float('inf')
        for i in nums:
            str_num = str(i)
            temp=0
            for j in str_num:
                temp+=int(j)
            result = min(result, temp)
        return result