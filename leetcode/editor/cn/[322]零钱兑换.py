# 给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。 
# 
#  计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。 
# 
#  你可以认为每种硬币的数量是无限的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3 
# 解释：11 = 5 + 5 + 1 
# 
#  示例 2： 
# 
#  
# 输入：coins = [2], amount = 3
# 输出：-1 
# 
#  示例 3： 
# 
#  
# 输入：coins = [1], amount = 0
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= coins.length <= 12 
#  1 <= coins[i] <= 2³¹ - 1 
#  0 <= amount <= 10⁴ 
#  
# 
#  Related Topics 广度优先搜索 数组 动态规划 👍 2160 👎 0
import functools
import math
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def coinChange(self, coins, amount):

        cache = [0] * (amount + 1)
        for i in range(1, amount+1):
            cache[i] = min((cache[i-c] for c in coins if i - c >= 0), default=math.inf) + 1
            # print(cache)
        return cache[-1] if cache[-1] != math.inf else -1

    def coinChange1(self, coins: List[int], amount: int) -> int:
        @functools.lru_cache(amount)
        def dp(rem) -> int:
            if rem < 0: return -1
            if rem == 0: return 0
            mini = int(1e9)
            for coin in self.coins:
                res = dp(rem - coin)
                if res >= 0 and res < mini:
                    mini = res + 1
            return mini if mini < int(1e9) else -1

        self.coins = coins
        if amount < 1: return 0
        return dp(amount)

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().coinChange([1,3,5], 7))