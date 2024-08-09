class Solution:
    def bestClosingTime(self, customers: str) -> int:
        result=0
        n=len(customers)
        cnt_y,cnt_n=customers.count('Y'),0
        result=[cnt_y,0]

        for i in range(1,n+1):
            prev_state=customers[i-1]
            if prev_state=='Y':
                cnt_y-=1
            else:
                cnt_n+=1
            
            if result[0]>(cnt_y+cnt_n):
                result=[cnt_y+cnt_n,i]
        
        return result[1]