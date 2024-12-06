class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        pos = list(set(list(range(1,n+1))) - set(banned))
        pos.sort()
        total_sum, cnt = 0, 0
        for i in pos:
            if total_sum+i<=maxSum:
                total_sum+=i
                cnt+=1
            else:
                break
        return cnt