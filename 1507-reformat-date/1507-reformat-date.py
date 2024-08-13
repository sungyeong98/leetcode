class Solution:
    def reformatDate(self, date: str) -> str:
        day={str(i)+'th':str(i) if i>=10 else '0'+str(i) for i in range(4,32)}
        day['1st']='01'
        day['2nd']='02'
        day['3rd']='03'
        month={"Jan":'01', "Feb":'02', "Mar":'03',
                "Apr":'04', "May":'05', "Jun":'06', 
                "Jul":'07', "Aug":'08', "Sep":'09', 
                "Oct":'10', "Nov":'11', "Dec":'12'}
        split_date=date.split(' ')[::-1]
        result=split_date[0]+'-'+month[split_date[1]]+'-'+day[split_date[2]]
        return result