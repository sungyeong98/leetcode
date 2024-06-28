from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict=defaultdict(int)
        for i in s:
            dict[i]+=1
        word_len=0
        for count in dict.values():
            word_len+=count//2*2
        odd_len=word_len + 1 if word_len<len(s) else word_len
        return odd_len