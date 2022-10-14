# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。 
# 
#  现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i -
#  1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。 
# 
#  求所能获得硬币的最大数量。 
# 
#  
# 示例 1：
# 
#  
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,5]
# 输出：10
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == nums.length 
#  1 <= n <= 300 
#  0 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 1113 👎 0


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def maxCoin(self, nums):
        def pick(left_nums, pre_coin):
            nonlocal max_coin
            # print(left_nums)
            n = len(left_nums)
            if n == 1:
                max_coin = max(max_coin, left_nums[0] + pre_coin)
                return

            for i in range(n):
                if i == 0:
                    curr_coin = left_nums[0] * left_nums[1]
                elif i == n - 1:
                    curr_coin = left_nums[-1] * left_nums[-2]
                else:
                    curr_coin = left_nums[i - 1] * left_nums[i] * left_nums[i + 1]
                curr_max = max(curr_max, curr_coin + pick(left_nums[:i] + left_nums[i + 1:]))

            return curr_max
        max_coin = 0
        return max_coin


    def maxCoins1(self, nums: List[int]) -> int:
        """
        dfs get answer, complexity O(n!)
        :param nums:
        :return:
        """
        def pick(left_nums):
            # print(left_nums)
            n = len(left_nums)
            if n == 0:
                return 1
            if n == 1:
                return left_nums[0]

            curr_max = 0
            for i in range(n):
                if i == 0:
                    curr_coin = left_nums[0] * left_nums[1]
                elif i == n - 1:
                    curr_coin = left_nums[-1] * left_nums[-2]
                else:
                    curr_coin = left_nums[i - 1] * left_nums[i] * left_nums[i + 1]
                curr_max = max(curr_max, curr_coin + pick(left_nums[:i] + left_nums[i + 1:]))

            return curr_max

        return pick(nums)


# leetcode submit region end(Prohibit modification and deletion)

print(Solution().maxCoins([7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]))
