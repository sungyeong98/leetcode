from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter=[Counter(word) for word in words]
        common_key=set.intersection(*[set(c.keys()) for c in counter])
        cnt={key:min(c[key] for c in counter) for key in common_key}

        result=[]
        for i in cnt:
            for _ in range(cnt[i]):
                result.append(i)

        return result