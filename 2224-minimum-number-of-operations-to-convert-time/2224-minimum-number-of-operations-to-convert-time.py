class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        cur=current.split(':')
        cor=correct.split(':')

        fixed_cur=int(cur[0])*60+int(cur[1])
        fixed_cor=int(cor[0])*60+int(cor[1])

        total_time=fixed_cor-fixed_cur
        result=0

        while total_time>0:
            if total_time>=60:
                result+=1
                total_time-=60
            elif total_time>=15:
                result+=1
                total_time-=15
            elif total_time>=5:
                result+=1
                total_time-=5
            else:
                result+=1
                total_time-=1
        
        return result