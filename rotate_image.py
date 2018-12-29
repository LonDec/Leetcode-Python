#!usr/bin/env/python2
# -*- coding: utf-8 -*-
# __author__ = 'herixth'
# __Date__   = 2018/12/29

class Solution:
    def rotate(self, matrix):
        """
        : type matrix: List[List[int]]
        : rtype: void Do not return anything, modify matrix in-place instead.
        """
        lens = len(matrix)
        for row in range(0, lens):
            for col in range(row, lens):
                matrix[row][col], matrix[col][row] = \
                matrix[col][row], matrix[row][col]
        for elem in matrix:
            elem.reverse()


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Solution().rotate(matrix)
    for elem in matrix:
        print (elem)
