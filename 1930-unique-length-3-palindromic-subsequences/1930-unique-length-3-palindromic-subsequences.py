class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        visited=set()
        left=defaultdict(int)
        right=Counter(s[1:])

        for i in range(1,n-1):
            prev_word, word, next_word = s[i-1], s[i], s[i+1]
            left[prev_word]+=1
            right[word]-=1
            
            if right[word]==0:
                right.pop(word)
            if left[word]==0:
                left.pop(word)

            for j in set(left.keys())&set(right.keys()):
                if j+word+j not in visited:
                    visited.add(j+word+j)

        return len(visited)