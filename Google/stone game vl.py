#Problem: 1686. Stone Game VI
#Link: https://leetcode.com/problems/stone-game-vi/



class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)
        stones = [(aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]) for i in range(n)]
        stones.sort(reverse=True, key=lambda x: x[0])
        alice_score, bob_score = 0, 0
        for turn, (_, alice_value, bob_value) in enumerate(stones):
            if turn % 2 == 0: 
                alice_score += alice_value
            else:  
                bob_score += bob_value
        if alice_score > bob_score:
            return 1
        elif alice_score < bob_score:
            return -1
        else:
            return 0