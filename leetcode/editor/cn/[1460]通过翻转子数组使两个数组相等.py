
# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def canBeEqual(self, target, arr) -> bool:
        c_t = Counter(target)
        c_a = Counter(arr)
        return c_t == c_a

# leetcode submit region end(Prohibit modification and deletion)
