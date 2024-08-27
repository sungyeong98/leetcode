class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank={val:idx+1 for idx,val in enumerate(sorted(set(arr)))}
        return list(map(rank.get,arr))