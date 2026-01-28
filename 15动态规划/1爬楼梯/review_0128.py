# 2024-01-28 review
class Solution:
    def climbStairs(self, n: int) -> int:
        dp_first = 1
        dp_second = 1
        for i in range(2, n+ 1):
            dp_temp = dp_first + dp_second
            dp_first = dp_second
            dp_second = dp_temp
        return dp_second
