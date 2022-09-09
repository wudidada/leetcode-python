# 给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  判断你是否能够到达最后一个下标。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 3 * 10⁴ 
#  0 <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics 贪心 数组 动态规划 👍 1994 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # 从后往前遍历
    # 有0的地方为隘口，进行标记，非0处判断能否跳过下一个没被跨过的隘口
    def canJump1(self, nums: List[int]) -> bool:
        n = len(nums)

        if n > 1 and nums[0] == 0:
            return False

        if n == 1:
            return True

        i = n - 1
        while i > -1:
            if nums[i] == 0:
                i -= 0
            else:
                break
            i -= 1
        zero_index = n - 2 if i != n - 1 else 0

        while i > -1:
            step = nums[i]
            if zero_index:
                if zero_index - i + 1 <= step:
                    zero_index = 0
            elif step == 0:
                zero_index = i
            i -= 1

        return zero_index == 0

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        max_step = 0
        n = len(nums)

        for i, num in enumerate(nums):
            # print(i, num, max_step)
            if num == 0:
                if max_step <= i and max_step + 1 < n:
                    return False
            else:
                max_step = max(max_step, i + num)
        return max_step + 1 >= n

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().canJump([3,2,1,0,4]))
