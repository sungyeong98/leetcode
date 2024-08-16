class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n=len(s)
        visited=set()
        left=defaultdict(int)
        right=Counter(s[1:])

        for i in range(1,n-1):
            prev_word, word = s[i-1], s[i]
            next_word = s[i+1]
            left[prev_word]+=1
            right[word]-=1
            if right[word]==0:
                right.pop(word)
            
            if right[prev_word]>0 and prev_word+word+prev_word not in visited:
                visited.add(prev_word+word+prev_word)
            if left[next_word]>0 and next_word+word+next_word not in visited:
                visited.add(next_word+word+next_word)

        return len(visited)