# -*- coding : utf-8 -*-


class Solustion:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = l1[::-1]
        l2 = l2[::-1]
        return int(l1) + int(l2)


def main():
    l1 = input('str_1:')
    l2 = input('str_2:')
    print(Solustion().addTwoNumbers(l1, l2))


if __name__ == "__main__":
    main()
