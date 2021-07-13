class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = int(n)
        ansstr = '1'
        nowstr = str()
        if n == 1:
            return ansstr
        else:
            for num in range(n - 1):
                count = 0
                loc = ansstr[0]
                for inc in range(len(ansstr)):
                    if ansstr[inc] == loc:
                        count += 1
                    else:
                        nowstr += str(count) + str(loc)
                        loc = ansstr[inc]
                        count = 1
                if count:
                    nowstr += str(count) + str(loc)
                ansstr = nowstr
                nowstr = str()
            return ansstr


def main():
    for n in range(10):
        print(str(n) + ' ' + Solution().countAndSay(n + 1))


if __name__ == "__main__":
    main()
