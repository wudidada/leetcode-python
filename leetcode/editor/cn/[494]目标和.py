# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
# 
#  Related Topics 数组 动态规划 回溯 👍 1406 👎 0
import functools
from collections import defaultdict
from leetcode.editor.cn.util import print_matrix
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findTargetSumWays(self, nums, target):
        nums_sum = sum(nums)
        neg, remain = (nums_sum - target) // 2, (nums_sum - target) % 2
        if neg < 0 or remain != 0:
            return 0

        matrix = [[0] * (neg + 1) for _ in range(2)]
        matrix[0][0] = 1
        for num in nums:
            for i in range(0, neg + 1):
                matrix[1][i] = matrix[0][i]
                if i >= num:
                    matrix[1][i] += matrix[0][i - num]
            matrix[0], matrix[1] = matrix[1], matrix[0]
            # print(f'======= {num} ==========')
            # print_matrix(matrix)
        return matrix[0][-1]

    def findTargetSumWays2(self, nums: List[int], target: int) -> int:
        @functools.cache
        def find_sum(i, t):
            if i == n:
                return 1 if t == 0 else 0

            return find_sum(i + 1, t + nums[i]) + find_sum(i + 1, t - nums[i])

        n = len(nums)
        return find_sum(0, target)

# leetcode submit region end(Prohibit modification and deletion)

Solution().findTargetSumWays([1,1,1,1,1], 3)
