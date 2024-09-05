class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3: return False
        vowels=set('aeiouAEIOU')
        special=set('@#$')

        word=set(word)
        if word & special:
            return False
        if not word & vowels:
            return False
        return word-(vowels|set(digits))