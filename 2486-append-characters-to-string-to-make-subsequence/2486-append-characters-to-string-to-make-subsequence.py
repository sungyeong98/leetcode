from collections import deque
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx, t_idx = 0, 0
        while s_idx < len(s) and t_idx < len(t):
            if t[t_idx]==s[s_idx]:
                t_idx+=1
                s_idx+=1
            else:
                s_idx+=1

        return len(t)-t_idx