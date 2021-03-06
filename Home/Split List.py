#  You have to split a given array into two arrays. If it has an odd amount of elements, then the first array should have more elements. If it has no elements, then two empty arrays should be returned.
#
# example
#
# Input: Array.
#
# Output: Array or two arrays.
#
# Example:
# split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
# split_list([1, 2, 3]) == [[1, 2], [3]]
#
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-split-list { 3 }

def split_list(items: list) -> list:
    # your code here
    if int(len(items)) == 0:
        return [[],[]]
    elif len(items) % 2 == 0:
        return [items[:int(len(items)/2)],items[int(len(items)/2):]]
    elif len(items) % 2 == 1:
        return [items[:int(len(items)/2) + 1],items[int(len(items)/2) + 1:]]



if __name__ == '__main__':
    print("Example:")
    print(split_list([1, 2, 3, 4, 5, 6]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Coding complete? Click 'Check' to earn cool rewards!")
