# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
# 
#  Related Topics 数组 二分查找 分治 👍 5771 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        full_array = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                full_array.append(nums1[i])
                i += 1
            else:
                full_array.append(nums2[j])
                j += 1

        full_array += nums1[i:]
        full_array += nums2[j:]
        return full_array[len(full_array) // 2] if len(full_array) % 2 == 1 else (full_array[len(full_array) // 2 - 1] + full_array[len(full_array) // 2]) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElenment(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    return nums2[index2+k-1]
                if index2 == n:
                    return nums1[index1+k-1]
                if k == 1:
                    return min(nums2[index2], nums1[index1])

                newIndex1 = min(index1+k//2-1, m-1)
                newIndex2 = min(index2+k//2-1, n-1)

                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElenment(totalLength//2+1)
        else:
            return (getKthElenment(totalLength//2) + getKthElenment(totalLength//2+1)) / 2



# leetcode submit region end(Prohibit modification and deletion)
test = Solution()
test.findMedianSortedArrays([1, 3], [2, 4, 5, 6])
