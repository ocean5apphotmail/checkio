#  Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.
#
# Input: Iterable
#
# Output: Iterable
#
# Example:
# frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
#  Precondition: elements can be ints or strings
#
# The mission was taken from Python CCPS 109 Fall 2018. It's being taught for Ryerson Chang School of Continuing Education by Ilkka Kokkarinen
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-frequency-sort { 10 }


def frequency_sort(items):
    # your code here

    rlist = []
    tdict = {}
    for el in items:
        if el not in tdict:
            tdict[el] = items.count(el)

    itemslist = sorted(tdict.items(),key=lambda x:x[1],reverse=True)

    for e in itemslist:
        for i in range(0, e[1]):
            rlist.append(e[0])

    return rlist



    # rlist = []
    # for idx, el in enumerate(sorted(data, key = lambda i: i['price'],reverse=True)):
    #     if idx == limit:
    #         return rlist
    #     else:
    #         rlist.append(el)
    # return rlist

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    assert list(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4])) == [4,4,4,4,2,2,2,6,6]
    print("Coding complete? Click 'Check' to earn cool rewards!")
