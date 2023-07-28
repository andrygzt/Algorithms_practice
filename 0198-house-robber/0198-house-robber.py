class Solution:
    def rob(self, nums: List[int]) -> int:
        def help(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(help(i-1), help(i-2) + nums[i])
            return memo[i]

        memo ={}
        return help(len(nums)-1)