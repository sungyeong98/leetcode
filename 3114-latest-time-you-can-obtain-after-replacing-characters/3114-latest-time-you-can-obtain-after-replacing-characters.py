class Solution:
    def findLatestTime(self, s: str) -> str:
        hour,minute=s.split(':')
        if hour=='??':
            fixed_hour='11'
        elif hour[0]=='?':
            if hour[1] in '01':
                fixed_hour='1'+hour[1]
            else:
                fixed_hour='0'+hour[1]
        elif hour[1]=='?':
            if hour[0]=='0':
                fixed_hour=hour[0]+'9'
            else:
                fixed_hour=hour[0]+'1'
        else:
            fixed_hour=hour
        
        if minute=='??':
            fixed_minute='59'
        elif minute[0]=='?':
            fixed_minute='5'+minute[1]
        elif minute[1]=='?':
            fixed_minute=minute[0]+'9'
        else:
            fixed_minute=minute
        
        return fixed_hour+':'+fixed_minute