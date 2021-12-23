#  中位数是一个可将数值集合划分为相等的上下两部分的一个数值。如果列表数据的个数是奇数，则列表中间那个数据就是列表数据的中位数；如果列表数据的个数是偶数，则列表中间那2个数据的算术平均值就是列表数据的中位数。在这个任务里，你将得到一个含有自然数的非空数组（X）。你必须把它分成上下两部分，找到中位数。
#
# 输入: 一个作为数组的整数(int)列表(list)的。
#
# 输出: 数组的中位数(int, float).
#
# 范例:
# checkio([1, 2, 3, 4, 5]) == 3
# checkio([3, 1, 2, 5, 3]) == 3
# checkio([1, 300, 2, 200, 1]) == 2
# checkio([3, 6, 20, 99, 10, 15]) == 12.5
# 1
# 2
# 3
# 4
#
# 如何使用： 中位数在概率论和统计学中得到应用，它偏态分布中有显著的价值。例如:我们想从一组数据中知道人们的平均财富 -- 100人一个月收入100美元，10人一个月收入1,000,000美元。如果我们算平均值，得到的是91000美元。这是一个完全没有向我们展示真实情况的奇怪的值。所以在这种情况下，中位数会给我们更有用的值和较好的描述。 维基百科的文章。
#
# 前提:
# 1 < len(data) ≤ 1000
# all(0 ≤ x < 10 ** 6 for x in data)
from typing import List

def checkio(data: List[int]) -> [int, float]:

    #replace this for solution
    return data[0]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print("Example:")
    print(checkio([1, 2, 3, 4, 5]))

    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("Coding complete? Click 'Check' to earn cool rewards!")
