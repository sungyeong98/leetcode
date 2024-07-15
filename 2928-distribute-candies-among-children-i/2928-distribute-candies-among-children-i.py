class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        nums=[i for i in range(limit+1)]
        result=0
        for i in product(nums,repeat=3):
            if sum(list(i))==n:
                result+=1
        return result