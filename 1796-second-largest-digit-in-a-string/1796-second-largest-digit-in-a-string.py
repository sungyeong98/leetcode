class Solution:
    def secondHighest(self, s: str) -> int:
        num=sorted(set([int(i) for i in s if i.isdigit()]))
        if len(num)<2:
            return -1
        return num[-2]