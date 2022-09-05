# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 1846 👎 0
import heapq
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    # 去掉比当前的k个元素还小的元素
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums[:k]:
            heapq.heappush(h, num)
        for num in nums[k:]:
            heapq.heappushpop(h, num)
        return h[0]

    # 去掉所有元素中最大值，进行k-1次
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def build_heap():
            for _ in range(nums_len // 2 - 1, -1, -1):
                heapify(_, nums_len)

        def heapify(index, size):
            l, r = index * 2 + 1, index * 2 + 2
            largest = index
            if l < size and nums[l] > nums[largest]:
                largest = l
            if r < size and nums[r] > nums[largest]:
                largest = r
            if largest != index:
                swap(index, largest)
                heapify(largest, size)

        def swap(i1, i2):
            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp

        nums_len = len(nums)
        build_heap()
        heap_size = nums_len
        for i in range(k-1):
            heap_size -= 1
            swap(0, heap_size)
            heapify(0, heap_size)
        return nums[0]
# leetcode submit region end(Prohibit modification and deletion)
