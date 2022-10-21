# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。 
# 
#  请你找出符合题意的 最短 子数组，并输出它的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
#  
#  
# 
#  
# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,4]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  
# 
#  进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？ 
# 
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈 👍 944 👎 0

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        reverse_max = 0
        max_index = 0

        for i in range(1, n):
            if nums[i] >= nums[max_index]:
                max_index = i
            else:
                reverse_max = i

        if reverse_max == 0:
            return 0

        reverse_min = n - 1
        min_index = n - 1
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[min_index]:
                min_index = i
            else:
                reverse_min = i
        return reverse_max - reverse_min + 1

    def findUnsortedSubarray1(self, nums: List[int]) -> int:
        """
        使用单调站栈保存之前数及下标 当出现逆序时方便找到最远的逆序的位置
        :param nums:
        :return:
        """
        n = len(nums)
        stack = []

        min_index, max_index = n, 0

        for i, num in enumerate(nums):
            while len(stack) > 0 and num < stack[-1][0]:
                min_index = min(min_index, stack.pop()[1])
                print(f'min_index: {min_index}')
            stack.append((num, i))
        stack.clear()

        if min_index == n:
            return 0

        for i in range(n-1, -1, -1):
            num = nums[i]
            while len(stack) > 0 and num > stack[-1][0]:
                max_index = max(max_index, stack.pop()[1])
                print(f'max_index: {max_index}')
            stack.append((num, i))
        return max_index - min_index + 1

# leetcode submit region end(Prohibit modification and deletion)
