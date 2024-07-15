class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        temp, nums = [j for i in grid for j in i], [i for i in range(1,n**2+1)]
        a, b = Counter(temp), Counter(nums)
        a.subtract(b)

        result=[0,0]
        for i in a:
            if a[i]==1:
                result[0]=i
            if a[i]==-1:
                result[1]=i
        return result