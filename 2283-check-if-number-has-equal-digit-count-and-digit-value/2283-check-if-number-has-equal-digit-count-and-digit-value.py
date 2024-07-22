class Solution:
    def digitCount(self, num: str) -> bool:
        n=Counter(num)
        for idx,val in enumerate(num):
            if n[str(idx)]!=int(val):
                return False
        return True