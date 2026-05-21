class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        dp0 = 1
        dp1 = 1
        curr = 0

        for i in range(2, n + 1):
            curr = dp0 + dp1
            dp0, dp1 = dp1, curr

        return curr