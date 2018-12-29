#!usr/bin/env/python2
# -*- coding: utf-8 -*-
# __author__ = 'herixth'
# __Date__ = 2018/12/29 

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        rowMax = len(matrix)
        colMax = 0
        if rowMax != 0:
            colMax = len(matrix[0])
        col_curr = -1
        row_curr = 0
        for cnt in range(rowMax * colMax):
            while col_curr + 1 < colMax and type(matrix[row_curr][col_curr + 1]) == int:
                col_curr += 1
                ans.append(matrix[row_curr][col_curr])
                matrix[row_curr][col_curr] = str(1)
                cnt +=1
            while row_curr + 1 < rowMax and type(matrix[row_curr + 1][col_curr]) == int:
                row_curr += 1
                ans.append(matrix[row_curr][col_curr])
                matrix[row_curr][col_curr] = str(1)
                cnt += 1
            while col_curr - 1 >= 0 and type(matrix[row_curr][col_curr - 1]) == int:
                col_curr -= 1
                ans.append(matrix[row_curr][col_curr])
                matrix[row_curr][col_curr] = str(1) 
                cnt += 1
            while row_curr - 1 >= 0 and type(matrix[row_curr - 1][col_curr]) == int:
                row_curr -= 1
                ans.append(matrix[row_curr][col_curr])
                matrix[row_curr][col_curr] = str(1)
                cnt += 1
        return ans


if __name__ == '__main__':
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print (Solution().spiralOrder(matrix))