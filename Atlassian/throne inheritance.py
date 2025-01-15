#Problem: 1600. Throne Inheritance
#Link: https://leetcode.com/problems/throne-inheritance/


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.family = {kingName: []}  
        self.dead = set()
        
    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.family:
            self.family[parentName] = []
        self.family[parentName].append(childName)
        self.family[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []

        def dfs(person):
            if person not in self.dead:
                order.append(person)
            for child in self.family.get(person, []):
                dfs(child)

        dfs(self.king)
        return order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()