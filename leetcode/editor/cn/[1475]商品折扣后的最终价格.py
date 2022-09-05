# 给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。 
# 
#  商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] 
# <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。 
# 
#  请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。 
# 
#  
# 
#  示例 1： 
# 
#  输入：prices = [8,4,6,2,3]
# 输出：[4,2,4,2,3]
# 解释：
# 商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
# 商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
# 商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
# 商品 3 和 4 都没有折扣。
#  
# 
#  示例 2： 
# 
#  输入：prices = [1,2,3,4,5]
# 输出：[1,2,3,4,5]
# 解释：在这个例子中，所有商品都没有折扣。
#  
# 
#  示例 3： 
# 
#  输入：prices = [10,1,1,6]
# 输出：[9,0,1,6]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 500 
#  1 <= prices[i] <= 10^3 
#  
# 
#  Related Topics 栈 数组 单调栈 👍 159 👎 0


from typing import List
# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def finalPrices1(self, prices: List[int]) -> List[int]:
        m = len(prices)
        prices.append(0)            # prices[-1]用于指示没有折扣
        discount = [0] * (m + 1)    # discount[i]记录第i个元素之后小于该元素的最大值的偏移
        discount[m-1] = -1
        for i in range(m-2, -1, -1):
            d_i = i + 1
            while d_i != -1 and prices[i] < prices[d_i]:
                d_i = discount[d_i]
            discount[i] = d_i
        return [prices[i] - prices[discount[i]] for i in range(m)]

    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        res = [0] * n
        st = [0]
        for i in range(n-1, -1, -1):
            while prices[i] < st[-1]:
                st.pop()
            res[i] = prices[i] - st[-1]
            st.append(prices[i])
        return res

# leetcode submit region end(Prohibit modification and deletion)
