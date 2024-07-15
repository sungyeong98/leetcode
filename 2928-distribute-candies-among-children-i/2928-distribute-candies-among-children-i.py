class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        #solution1
        '''
        nums=[i for i in range(limit+1)]
        result=0
        for i in product(nums,repeat=3):
            if sum(list(i))==n:
                result+=1
        return result
        '''

        #solution2
        result=0
        for i in range(min(n,limit)+1):
            for j in range(min(n-i,limit)+1):
                num=n-i-j
                if 0<=num<=limit:
                    result+=1
        return result