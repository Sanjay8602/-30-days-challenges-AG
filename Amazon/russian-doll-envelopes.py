#problem: https://leetcode.com/problems/russian-doll-envelopes/
#title: Russian Doll Envelopes


class Solution:
    def maxEnvelopes(self, e: List[List[int]]) -> int:
        e.sort(key=lambda x: (x[0], -x[1]))
        heights = [h for _, h in e]
        lis = []
        
        for h in heights:
            pos = bisect_left(lis, h)
            if pos == len(lis):
                lis.append(h) 
            else:
                lis[pos] = h  
        return len(lis)