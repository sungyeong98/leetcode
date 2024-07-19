class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb=deque(list(combinations(list(characters),combinationLength)))

    def next(self) -> str:
        if self.comb:
            return ''.join(self.comb.popleft())

    def hasNext(self) -> bool:
        if self.comb:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()