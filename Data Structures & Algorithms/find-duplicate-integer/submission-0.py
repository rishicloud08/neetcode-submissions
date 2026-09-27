class Solution:
    def findDuplicate(self, nums):
        slow = 0
        fast = 0

        # Find meeting point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Find duplicate
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow