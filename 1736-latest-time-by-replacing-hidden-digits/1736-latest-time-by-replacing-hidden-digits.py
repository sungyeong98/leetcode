class Solution:
    def maximumTime(self, time: str) -> str:
        hour,minute=time.split(':')
        fixed_hour,fixed_minute='',''
        if hour=='??':
            fixed_hour='23'
        elif hour[0]=='?':
            if hour[1] in '456789':
                fixed_hour='1'+hour[1]
            else:
                fixed_hour='2'+hour[1]
        elif hour[1]=='?':
            if hour[0] in '01':
                fixed_hour=hour[0]+'9'
            else:
                fixed_hour=hour[0]+'3'
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