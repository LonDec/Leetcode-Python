class Solution:
    def __init__(self):
        self.solutions = []  # the answer

    def check_(self, layers, curr):
        len_lay = len(layers)
        for idx in range(len_lay):
            if curr == layers[idx] or abs(curr - layers[idx]) == len_lay - idx:
                return False
        return True

    def creater(self, layers):
        """
        :type  layers: List[int]
        :rtype map
        """
        return map(lambda inf: ''.join(
            list(map(lambda idx: '.' if idx != inf else 'Q',
                     list(range(len(layers)))))),
            layers
        )

    def NQueen(self, n, layers=[]):
        """
        : type  n:      int
        : type  layers: List[int]
        : rtype null
        """
        if len(layers) == n:
            self.solutions.append(list(self.creater(layers)))
            return
        for inf in range(n):
            if (self.check_(layers, inf)):
                self.NQueen(n, layers + [inf])

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.NQueen(n)
        return self.solutions


if __name__ == '__main__':
    solution = Solution().solveNQueens(4)
    print(solution)
