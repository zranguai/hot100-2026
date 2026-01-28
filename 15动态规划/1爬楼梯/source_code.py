# solutin1 自顶向下
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i <= 1:
                return 1
            return dfs(i - 1) + dfs(i - 2)
        return dfs(n)
   
    
# solutin2 自底向上
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    
# solutin3 优化自底向上的空间复杂度为O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp_first, dp_second = 1, 1
        for i in range(2, n + 1):
            d_temp = dp_first + dp_second
            dp_first = dp_second
            dp_second = d_temp
        return dp_second