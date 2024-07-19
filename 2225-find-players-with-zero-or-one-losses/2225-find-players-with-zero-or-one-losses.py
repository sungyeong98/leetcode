class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        player={}
        for winner,loser in matches:
            if winner not in player:
                player[winner]=[1,0]
            else:
                player[winner][0]+=1
            if loser not in player:
                player[loser]=[0,1]
            else:
                player[loser][1]+=1
        
        all_winners=[i for i in player.keys() if sum(player[i])>0 and player[i][1]==0]
        one_lose_players=[i for i in player.keys() if sum(player[i])>0 and player[i][1]==1]

        return [sorted(all_winners), sorted(one_lose_players)]