class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result=[0]*num_people
        idx, cnt = 0, 1
        while candies>0:
            result[idx]+=min(cnt,candies)
            candies-=cnt
            cnt+=1
            idx=(idx+1)%num_people
        return result