class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        result=True
        for i in bits[-2::-1]:
            if i:
                result=not result
            else:
                break
        return result