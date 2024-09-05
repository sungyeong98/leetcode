class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_idx, type_idx = 0, 0
        while name_idx<=len(name) and type_idx<len(typed):
            if name_idx<len(name) and typed[type_idx]==name[name_idx]:
                type_idx+=1
                name_idx+=1
            elif typed[type_idx]==name[name_idx-1] and name_idx!=0:
                type_idx+=1
            else:
                return False
        return name_idx==len(name) and type_idx==len(typed)
            