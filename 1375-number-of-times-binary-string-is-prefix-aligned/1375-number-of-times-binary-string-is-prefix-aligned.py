class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        result=0
        n=len(flips)
        state=[False]*n
        check_point=0

        for i in range(n):
            idx=flips[i]-1
            state[idx]=True
            if i+1<=check_point:
                result+=1
            if all(state[:i+1]):
                result+=1
                check_point=i+1
        return result