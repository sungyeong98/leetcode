class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        num=[int(i) for i in s.split(' ') if i.isdigit()]

        return all(num[i]<num[i+1] for i in range(len(num)-1))