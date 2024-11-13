from bisect import bisect_left, bisect_right

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        nums.sort()
        ans = 0
        for i in range(len(nums) - 1):
            low = bisect_left(nums, lower - nums[i], i + 1)
            up = bisect_right(nums, upper - nums[i], i + 1)
            ans += up - low
        return ans
        