from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int: 
        curr = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                curr+=1
                maxcount = max(curr,maxcount)
            else:
                curr = 0
        return maxcount            