class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        
        while hand:
            num=min(hand)
            for i in range(groupSize):
                if num+i not in hand:
                    return False
                hand.pop(hand.index(num+i))
        
        return True