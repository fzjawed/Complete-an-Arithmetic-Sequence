class Solution:
    def solve(self, nums): 
        nums = sorted(nums)  
        import math
        factor = math.ceil(abs((nums[0]+nums[(len(nums)-1)])/(len(nums)+1)))
        if len(nums) > 2:
            for i in range(len(nums)-1):
                if (nums[i+1]-nums[i]) != factor:
                    missing = nums[i] + factor
                if nums[i] == nums[i+1]:
                    missing = 0
            return missing

        else:
            missing = ((nums[0]+nums[1])//2)
            return missing