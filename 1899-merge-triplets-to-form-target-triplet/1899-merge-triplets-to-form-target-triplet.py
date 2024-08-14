class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        result=[i for i in triplets if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]]
        if not result:
            return False

        for idx, seq in enumerate(list(zip(*result))):
            if target[idx] not in seq:
                return False
        
        return True