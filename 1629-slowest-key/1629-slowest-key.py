class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keys={i:0 for i in set(keysPressed)}
        for idx,val in enumerate(keysPressed):
            if idx==0:
                keys[val]=max(keys[val],releaseTimes[idx])
            else:
                keys[val]=max(keys[val], releaseTimes[idx]-releaseTimes[idx-1])
        result=sorted(keys.items(), key=lambda x:(-x[1],-ord(x[0])))
        return result[0][0]