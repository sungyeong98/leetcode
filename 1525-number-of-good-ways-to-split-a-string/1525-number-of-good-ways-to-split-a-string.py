class Solution:
    def numSplits(self, s: str) -> int:
        left_count=defaultdict(int)
        right_count=defaultdict(int)

        for i in s:
            right_count[i]+=1

        distinct_left=0
        distinct_right=len(right_count)

        result=0

        for i in range(len(s)-1):
            word=s[i]

            left_count[word]+=1
            if left_count[word]==1:
                distinct_left+=1
            
            right_count[word]-=1
            if right_count[word]==0:
                distinct_right-=1
            
            if distinct_left==distinct_right:
                result+=1
        return result