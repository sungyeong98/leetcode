class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        temp=defaultdict(int)
        for num in nums:
            bin_num=bin(num)[2:][::-1]
            for n in range(len(bin_num)):
                if bin_num[n]=='1':
                    temp[n]+=1
        result=0
        for i in temp:
            if temp[i]>=k:
                result+=2**i
        return result