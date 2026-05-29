from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        for ch in counter_t:
            if counter_t[ch] != counter_s[ch]:
                return ch      