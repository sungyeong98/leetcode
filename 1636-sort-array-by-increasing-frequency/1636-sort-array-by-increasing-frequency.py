class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        result,n=[],Counter(nums)
        n=sorted(n.items(), key=lambda x:(x[1],-x[0]))
        for num,cnt in n:
            result+=[num]*cnt
        return result