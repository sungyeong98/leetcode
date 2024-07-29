class Solution:
    def countSubstrings(self, s: str) -> int:
        #solution1
        '''
        result=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    result+=1
        return result
        '''
        output = 0
        length = len(s)
        current = 0


        while current < length:
            left = current
            right = current
            flag = False

            while (left > 0) and (s[left - 1] == s[current]):
                left -= 1

            while (right < (length - 1)) and (s[right + 1] == s[current]):
                right += 1
                flag = True
            
            if flag:
                n = right - left + 1
                output += int(n * (n+1) / 2) - 1
                current = right
                continue

            while (left > 0) and (right < (length - 1)) and (s[left - 1] == s[right + 1]):
                left -= 1
                right += 1
                output += 1
            
            output += 1
            current += 1
            
        return output