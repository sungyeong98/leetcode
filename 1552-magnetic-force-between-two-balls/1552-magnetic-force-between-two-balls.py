class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left,right=1,position[-1]-position[0]
        answer=-1
        while left<=right:
            mid=left+(right-left)//2
            prev_position, balls = position[0], 1
            for i in range(1,len(position)):
                if position[i]-prev_position>=mid:
                    prev_position=position[i]
                    balls+=1
            if balls>=m:
                answer=mid
                left=mid+1
            else:
                right=mid-1
        return answer