class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n=len(nums)
        counter=Counter(nums)
        cnt=defaultdict(int)

        for i in range(n-1):
            num=nums[i]
            counter[num]-=1
            if counter[num]==0:
                counter.pop(num)
            for j in counter:
                cnt[abs(num-j)]+=counter[j]
        cnt=dict(sorted(cnt.items(), key=lambda x:x[0]))

        result=0
        for i in cnt:
            if cnt[i]<k:
                k-=cnt[i]
            else:
                return i