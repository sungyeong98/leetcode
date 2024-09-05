class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n=len(nums)
        temp=set()
        for i in range(n):
            temp.add(nums[i][i])
            temp.add(nums[n-1-i][i])
        
        result=[]
        for num in list(temp)[::-1]:
            flag=True
            for i in range(2,int(math.sqrt(num))+1):
                if num%i==0:
                    flag=False
                    break
            if flag:
                result.append(num)
        return max(result) if result else 0