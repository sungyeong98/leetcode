class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        cnt, idx1, idx2 = 0, 0, 0
        while(idx1<len(str1)):
            if (0<=ord(str2[idx2])-ord(str1[idx1])<=1) or (str1[idx1]=='z' and str2[idx2]=='a'):
                cnt+=1
                if cnt==len(str2):
                    return True
                idx1+=1
                idx2+=1
            else:
                idx1+=1
        
        return len(str2)==cnt