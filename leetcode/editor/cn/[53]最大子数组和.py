# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
# 
#  子数组 是数组中的一个连续部分。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,4,-1,7,8]
# 输出：23
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
# 
#  进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。 
#  Related Topics 数组 分治 动态规划 👍 4100 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        total_max, current_max = nums[0], nums[0]
        for num in nums[1:]:
            current_max = max(0, current_max)
            current_max += num
            total_max = max(total_max, current_max)
        return total_max

    def maxSubArray2(self, nums: List[int]) -> int:
        total, floor = 0, 0
        res = nums[0]
        for num in nums:
            total += num
            res = max(total - floor, res)
            floor = min(floor, total)
            # print(total, floor, res)
        return res

    def maxSubArray(self, nums: List[int]) -> int:
        def maxSub(left, right):
            if left == right:
                return nums[left]

            mid = (left + right) // 2
            return max(maxSub(left, mid), maxSub(mid + 1, right), maxMid(left, mid, right))

        def maxMid(left, mid, right):
            total = nums[mid] + nums[mid + 1]
            left_max, right_max = 0, 0
            left_total, right_total = 0, 0
            for n in nums[left:mid][::-1]:
                left_total += n
                left_max = max(left_max, left_total)

            for n in nums[mid + 2:right + 1]:
                right_total += n
                right_max = max(right_max, right_total)
            return total + left_max + right_max

        return maxSub(0, len(nums) - 1)


# leetcode submit region end(Prohibit modification and deletion)

# Solution().maxSubArray([5,4,-1,7,8])
s = Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(s)
