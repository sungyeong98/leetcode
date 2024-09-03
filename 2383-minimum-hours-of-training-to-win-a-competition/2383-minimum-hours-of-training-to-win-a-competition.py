class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        result,n=0,len(energy)
        for i in range(n):
            while initialEnergy<=energy[i] or initialExperience<=experience[i]:
                if initialEnergy<=energy[i]:
                    initialEnergy+=1
                    result+=1
                if initialExperience<=experience[i]:
                    initialExperience+=1
                    result+=1
            initialEnergy-=energy[i]
            initialExperience+=experience[i]
        return result