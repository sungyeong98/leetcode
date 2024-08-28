class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        nums=Counter(ranks)
        shapes=Counter(suits)
        if len(shapes)==1:
            return 'Flush'
        elif len(nums)<=3:
            return 'Three of a Kind'
        elif len(nums)<=4:
            return 'Pair'
        else:
            return 'High Card'