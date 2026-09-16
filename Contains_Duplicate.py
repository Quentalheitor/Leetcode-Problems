class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        x = nums[0]
        for i in nums[1:]:
            if x == i:
                return True
            x = i
        return False