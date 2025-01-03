#problem: Bulls and Cows
#leetcode: 299
#URL: https://leetcode.com/problems/bulls-and-cows/


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        

        bulls = 0
        cows = 0
        secret_count = [0] * 10
        guess_count = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[ord(secret[i]) - ord('0')] += 1
                guess_count[ord(guess[i]) - ord('0')] += 1
        for i in range(10):
            cows += min(secret_count[i], guess_count[i])

        return f"{bulls}A{cows}B"