# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#  
# 
#  示例 2: 
# 
#  
# 输入: nums = [1], k = 1
# 输出: [1] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  k 的取值范围是 [1, 数组中不相同的元素的个数] 
#  题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的 
#  
# 
#  
# 
#  进阶：你所设计算法的时间复杂度 必须 优于 O(n log n) ，其中 n 是数组大小。 
# 
#  Related Topics 数组 哈希表 分治 桶排序 计数 快速选择 排序 堆（优先队列） 👍 1306 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def build_heap():
            for i in range(k//2-1, -1, -1):
                heapify(i)

        def heapify(i):
            nonlocal frequency
            l, r = i * 2 + 1, i * 2 + 2
            smallest = i
            if l < k and frequency[l][1] < frequency[smallest][1]:
                smallest = l
            if r < k and frequency[r][1] < frequency[smallest][1]:
                smallest = r
            if smallest != i:
                swap(i, smallest)
                heapify(smallest)

        def heap_replace(i):
            if frequency[i][1] < frequency[0][1]:
                return

            swap(0, i)
            heapify(0)

        def swap(i, j):
            nonlocal frequency
            temp = frequency[i]
            frequency[i] = frequency[j]
            frequency[j] = temp

        counter = {}
        for num in nums:
            counter[num] = (counter.get(num) or 0) + 1

        frequency = [(k, v) for k, v in counter.items()]
        # print(frequency)
        build_heap()
        # print(frequency)
        for _ in range(k, len(frequency)):
            heap_replace(_)
            # print(frequency)

        return [_[0] for _ in frequency[:k]]

# leetcode submit region end(Prohibit modification and deletion)

Solution().topKFrequent([4,1,-1,2,-1,2,3], 2)