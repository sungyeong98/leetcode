class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        result=0
        while word in sequence:
            result+=sequence.count(word)
            sequence=sequence.replace(word,'')
        return result