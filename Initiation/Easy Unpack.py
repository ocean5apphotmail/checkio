#  在这里你的任务是创建得到一个元组，并返回一个包含三个元素（第一，第三和倒数第二的给定元组）的元组与的功能。
#
# example
#
# 输入: 一个不少于三个元素的元组
#
# 输出: 一个元组.
#
# 举个栗子:
#
# easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
# easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# easy_unpack((6, 3, 7)) == (6, 7, 3)
def easy_unpack(elements: tuple) -> tuple:
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    # your code here

    return (list(elements)[0],list(elements)[2],list(elements)[-2])


if __name__ == '__main__':
    print('Examples:')
    print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
    assert easy_unpack((6, 2, 9, 4, 3, 9)) == (6, 9, 3)
    assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
    assert easy_unpack((6, 3, 7)) == (6, 7, 3)
    print('Done! Go Check!')