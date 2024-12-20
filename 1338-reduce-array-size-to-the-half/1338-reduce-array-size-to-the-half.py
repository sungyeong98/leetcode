class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n=len(arr)
        cnt=Counter(arr)
        cnt=dict(sorted(cnt.items(), key=lambda x:-x[1]))
        target=n//2

        result,cur=0,0
        for i in cnt:
            cur+=cnt[i]
            result+=1
            if cur>=target:
                return result
        