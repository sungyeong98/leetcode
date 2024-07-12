class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x>y:
            score1,ss=self.gain_x(s,x)
            score2,_=self.gain_y(ss,y)
            return score1+score2
        else:
            score1,ss=self.gain_y(s,y)
            score2,_=self.gain_x(ss,x)
            return score1+score2

    def gain_y(self,s,y):
        score=0
        while 'ba' in s:
            l=len(s)
            s=s.split('ba')
            s=''.join([i for i in s if i])

            score+=y*((l-len(s))//2)
        return score,s
    
    def gain_x(self,s,x):
        score=0
        while 'ab' in s:
            l=len(s)
            s=s.split('ab')
            s=''.join([i for i in s if i])

            score+=x*((l-len(s))//2)
        return score,s