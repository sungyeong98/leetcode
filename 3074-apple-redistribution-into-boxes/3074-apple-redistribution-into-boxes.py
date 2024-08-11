class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        result=0
        capacity.sort(reverse=True)
        total_apple=sum(apple)
        for c in capacity:
            result+=1
            total_apple-=c
            if total_apple<=0:
                break
        return result