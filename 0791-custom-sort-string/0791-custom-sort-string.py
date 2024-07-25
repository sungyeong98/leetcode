class Solution:
    def customSortString(self, order: str, s: str) -> str:
        temp={val:idx for idx,val in enumerate(order)}
        char=Counter(s)
        save_list=list(set(s))
        result=''
        for i in temp:
            if i in save_list:
                result+=i*char[i]
                save_list.pop(save_list.index(i))
        while save_list:
            a=save_list.pop()
            result+=a*char[a]
        return result