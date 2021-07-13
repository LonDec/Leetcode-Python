# -*- coding: utf-8 -*-


class Solution:
    def is_palindrome(self, s):
        wai = s[::-1]
        return wai == s

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        anslen = -1
        lens = len(s)
        for inc in range(lens):
            for snc in range(inc):
                sam = s[snc:inc + 1]
                if Solution().is_palindrome(sam):
                    if len(sam) >= anslen:
                        anslen = len(sam)
                        ansstr = sam
        return ansstr


def main():
    s = input('input str:')
    print(Solution().longestPalindrome(s))


if __name__ == "__main__":
    main()
