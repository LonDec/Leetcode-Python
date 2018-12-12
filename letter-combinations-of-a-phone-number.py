# -*- UTF-8 -*-


class Solution:
    def dfs(self, ToList, currList, curr, lens, strs, nums):
        if curr == lens:
            ToList.append(currList)
            return
        for elem in nums[strs[curr]]:
            self.dfs(ToList, currList + elem, curr + 1, lens, strs, nums)
        pass

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = { '2': ['a', 'b', 'c'], 
                 '3': ['d', 'e', 'f'], 
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']
                }
        lens = len(digits)
        ToList = []
        self.dfs(ToList, "", 0, lens, digits, nums)
        return ToList        


if __name__ == '__main__':
    so = Solution()
    List = so.letterCombinations("23")
    print (List)