class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climbHelper(num):
            if num <= 1:
                return 1
            
            if num in memo:
                return memo[num]

            memo[num] = climbHelper(num - 1) + climbHelper(num - 2)
            return memo[num]

        return climbHelper(n)