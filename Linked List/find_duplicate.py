class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


# make sure you understand the iteration through linked lists


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for n in nums:
            if n in seen:
                return n
            seen.add(n)


# this is a solution for list, pretty nice that i got it easily!
