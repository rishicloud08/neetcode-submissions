class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        value = 0
        freq = 0

        for i in set(nums):
            count=0
            for j in range(len(nums)):
                if i == nums[j]:
                    count+=1

            if count > freq:
                value = i
                freq = count
        return value      

                   

            
