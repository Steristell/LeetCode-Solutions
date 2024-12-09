class Solution(object):
    def isArraySpecial(self, nums, queries):
        #n = len(nums)
        store, ans = [], []

        for i in range(1, len(nums)):
            if (nums[i] % 2) == (nums[i - 1] % 2):
                store.append(i)

        for left, right in queries:
            idx = bisect_right(store, left)

            if idx < len(store) and  store[idx] <= right: ans.append(False)
            else: ans.append(True)
        
        return ans
            