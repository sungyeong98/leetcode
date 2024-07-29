class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result=0
        n=len(rating)

        for i in range(n):
            left_s,left_l=0,0
            right_s,right_l=0,0

            for j in range(i):
                if rating[j]<rating[i]:
                    left_s+=1
                if rating[j]>rating[i]:
                    left_l+=1
                
            for k in range(i+1,n):
                if rating[k]<rating[i]:
                    right_s+=1
                if rating[k]>rating[i]:
                    right_l+=1
            
            result+=left_s*right_l+left_l*right_s
        return result