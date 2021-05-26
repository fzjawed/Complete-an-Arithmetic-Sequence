class Solution:
    def solve(self, nums):
        s = sum(nums)
        return (nums[0] + nums[-1]) * (len(nums) + 1) // 2 - s