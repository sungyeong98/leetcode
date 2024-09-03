class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in "!?',;.":
            paragraph=paragraph.replace(i,' ')
        p=paragraph.split(' ')
        p=[i for i in p if i!='']
        cnt=defaultdict(int)
        for i in p:
            cnt[i.lower()]+=1
        for i in banned:
            if i in cnt:
                cnt.pop(i)
        return sorted(cnt.keys(), key=lambda x:cnt[x])[-1]