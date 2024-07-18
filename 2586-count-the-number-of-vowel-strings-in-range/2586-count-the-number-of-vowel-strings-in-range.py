class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel=['a','e','i','o','u']
        words=words[left:right+1]
        result=0
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                result+=1
        return result