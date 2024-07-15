class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        result=defaultdict(int)

        for val, wei in items1:
            result[val]+=wei
        for val, wei in items2:
            result[val]+=wei

        return list(sorted(result.items(), key=lambda x:x[0]))