#  You are given two strings and you have to find an index of the second occurrence of the second string in the first one.
#
# Let's go through the first example where you need to find the second occurrence of "s" in a word "sims". It’s easy to find its first occurrence with a function index or find which will point out that "s" is the first symbol in a word "sims" and therefore the index of the first occurrence is 0. But we have to find the second "s" which is 4th in a row and that means that the index of the second occurrence (and the answer to a question) is 3.
#
# Input: Two strings.
#
# Output: Int or None
#
# Example:
# second_index("sims", "s") == 3
# second_index("find the river", "e") == 12
# second_index("hi", " ") is None
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-second-index { 18 }

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code here
    p1 = text.find(symbol)
    if p1 == -1:
        return None
    p2 = text[p1+1:].find(symbol)
    if p2 == -1:
        return None
    else:
        return p2 + p1 + 1


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
