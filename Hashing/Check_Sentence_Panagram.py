"""
Date:18/04/2021
5734. Check if the Sentence Is Pangram - Leetcode Easy
The following problem is solved using set
"""
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        S=set()
        for s in sentence:
            S.add(s)
        if len(S)==26:
            return True
        return False
        