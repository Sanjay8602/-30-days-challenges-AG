# Problem: Friends of Appropriate Age
# Source: https://leetcode.com/problems/friends-of-appropriate-ages/



class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_count = Counter(ages)
        requests = 0
        for age_x in age_count:
            for age_y in age_count:
                if age_y <= 0.5 * age_x + 7:
                    continue
                if age_y > age_x:
                    continue
                if age_y > 100 and age_x < 100:
                    continue
                if age_x == age_y:
                    requests += age_count[age_x] * (age_count[age_x] - 1)
                else:
                    requests += age_count[age_x] * age_count[age_y]

        return requests