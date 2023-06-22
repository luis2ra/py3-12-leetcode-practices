'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto 
the end of the merged string.

Return the merged string.
'''

class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        cycles = min(len(word1), len(word2))
        print(cycles)
        merged = ""
        for i in range(cycles):
            merged += word1[i] + word2[i]
        if len(word1) == cycles:
            merged += word2[cycles:]
        if len(word2) == cycles:
            merged += word1[cycles:]
        return merged


word1 = input().lower()
word2 = input().lower()
solution = Solution()
merged = solution.merge_alternately(word1, word2)
print(merged)
