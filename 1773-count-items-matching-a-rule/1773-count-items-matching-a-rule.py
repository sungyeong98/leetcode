class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        result=0
        if ruleKey=='type':     idx=0
        elif ruleKey=='color':  idx=1
        else:                   idx=2

        for i in items:
            if i[idx]==ruleValue:
                result+=1
        return result