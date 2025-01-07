#Problem: Shopping Offers
#Link: https://leetcode.com/problems/shopping-offers/
#Best Solution using DFS


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        def dfs(needs):
            if tuple(needs) in memo:
                return memo[tuple(needs)]
            cost = sum(need * p for need, p in zip(needs, price))
            for offer in special:
                new_needs = [needs[i] - offer[i] for i in range(len(needs))]
                if all(x >= 0 for x in new_needs):
                    cost = min(cost, offer[-1] + dfs(new_needs))
            memo[tuple(needs)] = cost
            return cost
    
        memo = {}
        return dfs(needs)