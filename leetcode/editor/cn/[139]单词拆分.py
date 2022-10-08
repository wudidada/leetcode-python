# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。 
# 
#  注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
#  
# 
#  示例 2： 
# 
#  
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
#  
# 
#  示例 3： 
# 
#  
# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 300 
#  1 <= wordDict.length <= 1000 
#  1 <= wordDict[i].length <= 20 
#  s 和 wordDict[i] 仅有小写英文字母组成 
#  wordDict 中的所有字符串 互不相同 
#  
# 
#  Related Topics 字典树 记忆化搜索 哈希表 字符串 动态规划 👍 1828 👎 0
from collections import defaultdict
from typing import List
from leetcode.editor.cn.util import print_matrix


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def wordBreak(self, s, wordDict):
        """
        find all possible divide of s by length of words,
        if every part of one divide is in words, then it's ok
        :param s:
        :param wordDict:
        :return:
        """

        def break_ok(i, j):
            if (i, j) in cache:
                return False

            length = j - i + 1
            if length < length_sort[0]:
                return False

            if s[i: j+1] in words[length]:
                return True

            # one step forward
            for l in length_sort:
                # one possible step
                if s[i: i + l] in words[l]:
                    # depth first, go next step
                    if break_ok(i + l, j):
                        return True
            cache.add((i, j))
            return False

        words = defaultdict(set)
        for w in wordDict:
            words[len(w)].add(w)
        length_sort = sorted(words.keys())
        # record failed steps, successful steps will return immediately
        cache = set()
        return break_ok(0, len(s)-1)

    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        """
        this way will find out all sub str of s if they can be break
        which is redundant, because the length of words is fixed, and we only need to know if s is ok.
        :param s:
        :param wordDict:
        :return:
        """
        words = set(wordDict)
        n = len(s)
        # matrix[i][j] represent s[i:j+1] in wordDict or not
        matrix = [[False] * n for _ in range(n)]
        for step in range(1, n + 1):
            for start in range(n - step + 1):
                end = start + step - 1
                if s[start:end + 1] in words:
                    matrix[start][end] = True
                    # print(f'find: {s[start:end+1]}')
                    # print_matrix(matrix)
                    continue

                for i in range(start, end):
                    if matrix[start][i] and matrix[i + 1][end]:
                        matrix[start][end] = True
                        # print(f'find: {s[start:end+1]}')
                        # print_matrix(matrix)
                        break

        return matrix[0][n - 1]


# leetcode submit region end(Prohibit modification and deletion)
# print(Solution().wordBreak("ab", ["a", "b"]))
print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
