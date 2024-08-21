class Solution:
    def capitalizeTitle(self, title: str) -> str:
        fixed_str=[i[:1].upper()+i[1:].lower() if len(i)>2 else i.lower() for i in title.split(' ')]
        return ' '.join(fixed_str)