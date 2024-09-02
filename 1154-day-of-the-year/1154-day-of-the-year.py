from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        year,month,day=date[:4],date[5:7],date[8:]
        d1=datetime.strptime(year+'01'+'01','%Y%m%d')
        d2=datetime.strptime(''.join(date.split('-')),'%Y%m%d')
        diff=d2-d1
        return diff.days+1