# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  测试用例的答案是一个 32-位 整数。 
# 
#  子数组 是数组的连续子序列。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  -10 <= nums[i] <= 10 
#  nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数 
#  
# 
#  Related Topics 数组 动态规划 👍 1821 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = pre_product = pre_min_product = nums[0]
        for num in nums[1:]:
            curr_product = max(pre_product * num, num, pre_min_product * num)
            curr_min_product = min(pre_min_product * num, pre_product * num, num)
            max_product = max(max_product, curr_product)
            # print(f'{num}: \t\t{curr_product:10d} \t\t{curr_min_product:10d} \t\t{max_product:10d}')
            pre_min_product = curr_min_product
            pre_product = curr_product
        return max_product
# leetcode submit region end(Prohibit modification and deletion)
# Solution().maxProduct([2, 3, -2, 4])
# Solution().maxProduct([-2,3,-4])
Solution().maxProduct([-1,-2,-9,-6])