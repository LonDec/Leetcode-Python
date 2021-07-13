# -*- coding: utf-8 -*-

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens = len(nums)
        steps = list(range(lens))
        for idx in range(1, lens):
            steps[idx] = 0x0FFFFFF
            for pre in range(0, idx):
                if pre + nums[pre] >= idx:
                    steps[idx] = min(steps[idx], steps[pre] + 1)
        return steps[lens - 1]

if __name__ == '__main__':
    n = [2, 3, 1, 1, 4]
    su = Solution()
    print (su.jump(n))
