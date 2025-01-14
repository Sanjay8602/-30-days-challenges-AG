#Problem: Find Beautiful Indices in the Given Array I
#URL: https://leetcode.com/problems/find-beautiful-indices-in-the-given-array-i/submissions/1508694531/


class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n= len(s)
        la= len(a)
        lb= len(b)
        
        indices_a = [i for i in range(n - la + 1) if s[i:i + la] == a]
        indices_b = [j for j in range(n - lb + 1) if s[j:j + lb] == b]

        result = []
        j = 0
        for i in indices_a:
            while j < len(indices_b) and indices_b[j] < i - k:
                j += 1

            if j < len(indices_b) and abs(indices_b[j] - i) <= k:
                result.append(i)

        return result