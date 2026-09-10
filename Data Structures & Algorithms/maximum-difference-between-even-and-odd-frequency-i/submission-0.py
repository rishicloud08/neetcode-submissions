from collections import Counter
class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s).values()
        max_odd = max(c for c in counts if c % 2!= 0)
        min_even = min(c for c in counts if c % 2 == 0)

        return max_odd - min_even

