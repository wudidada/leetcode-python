# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics 数组 动态规划 👍 1530 👎 0

from typing import List
from leetcode.editor.cn.util import print_matrix


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def canPartition(self, nums):
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        partition_sum = nums_sum // 2
        n = len(nums)

        matrix = [[False] * (partition_sum + 1) for _ in range(2)]
        matrix[0][0] = True
        if nums[0] <= partition_sum:
            matrix[0][nums[0]] = True

        for num in nums[1:]:
            for j in range(partition_sum + 1):
                matrix[1][j] = matrix[0][j]
                if not matrix[1][j] and j >= num:
                    matrix[1][j] = matrix[0][j - num]
            matrix[0], matrix[1] = matrix[1], matrix[0]
            # print(f'======={num}=========')
            # print_matrix(matrix)
        return matrix[0][-1]

    def canPartition1(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2 == 1:
            return False

        partition_sum = nums_sum // 2
        sums = {0}
        for num in nums:
            num_sums = set()
            for s in sums:
                n_s = num + s
                if n_s == partition_sum:
                    return True
                elif n_s < partition_sum:
                    num_sums.add(n_s)
            sums.update(num_sums)
        return False


# leetcode submit region end(Prohibit modification and deletion)
Solution().canPartition([1, 2, 5])
