class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king=kingName
        self.people={kingName:[]}
        self._death=set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.people:
            self.people[parentName].append(childName)
        else:
            self.people[parentName]=[childName]
        self.people[childName]=[]

    def death(self, name: str) -> None:
        self._death.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order=[]
        self.dfs(self.king, order)
        return order

    def dfs(self, cur, order):
        if cur not in self._death:
            order.append(cur)
        for child in self.people[cur]:
            self.dfs(child, order)


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()