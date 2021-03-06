# 统计所有小于非负整数 n 的质数的数量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 10
# 输出：4
# 解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#  
# 
#  示例 2： 
# 
#  输入：n = 0
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：n = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 5 * 106 
#  
#  Related Topics 数组 数学 枚举 数论 
#  👍 707 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
from collections import OrderedDict


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [False] * n
        count = 0
        for i in range(2, n):
            if nums[i]:
                continue

            if not nums[i]:
                count += 1
                for x in range(i, n, i):
                    nums[x] = True
        return count
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    Solution().countPrimes(499979)
