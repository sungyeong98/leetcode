class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        temp=[0]
        for i in nums:
            temp.append(temp[-1]+i)
        result=[]
        for q in queries:
            result.append(bisect.bisect(temp,q)-1)
        return result