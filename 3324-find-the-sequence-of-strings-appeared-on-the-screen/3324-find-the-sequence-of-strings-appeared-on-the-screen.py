class Solution:
    def stringSequence(self, target: str) -> List[str]:
        result = []
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        prev = ''
        for char in target:
            idx = 0
            while idx < 26:
                if alphabet[idx] == char:
                    x = prev + alphabet[idx]
                    result.append(x)
                    prev = x
                    break
                else:
                    result.append(prev + alphabet[idx])
                idx += 1
        return result