class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        cnt=Counter(arr)
        target_list=[i for i in cnt.keys() if cnt[i]==1]
        result=[i for i in arr if i in target_list]
        if len(result)<k:
            return ''
        return result[k-1]