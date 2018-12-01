class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []


        def dfs(stsr, left, right, ans):
            if len(stsr) == 2 * n:
                ans.append(stsr)
                return
            if left < n:
                dfs(stsr + '(', left + 1, right, ans)
            if right < left:
                dfs(stsr + ')', left, right + 1, ans)

        dfs('', 0, 0, ans)
        return ans


if __name__ == '__main__':
    n = input()
    so = Solution()
    print(so.generateParenthesis(int(n)))
