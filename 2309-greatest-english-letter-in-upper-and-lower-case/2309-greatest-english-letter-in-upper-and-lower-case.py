class Solution:
    def greatestLetter(self, s: str) -> str:
        valid,not_valid=[],[]
        for i in s:
            if i.upper() in not_valid:
                continue

            if i.upper() in s and i.lower() in s:
                valid.append(i.upper())
            else:
                not_valid.append(i.upper())
        if not valid:   return ''
        return max(valid)