class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        result = []
        for i in range(len(nums)-k+1):
            sublist = nums[i:i+k]
            counter = sorted(Counter(sublist).items(), key=lambda x:(-x[1],-x[0]))
            temp=0
            for j in range(min(x,len(counter))):
                temp+=counter[j][0]*counter[j][1]
            result.append(temp)
        return result