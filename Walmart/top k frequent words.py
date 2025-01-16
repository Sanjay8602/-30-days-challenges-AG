#Problem: Given a non-empty list of words, return the k most frequent elements.
#Source: https://leetcode.com/problems/top-k-frequent-words/


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq={}
        for i in words:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        sorted_words = sorted(freq.keys(), key=lambda word: (-freq[word], word))
        return sorted_words[:k]