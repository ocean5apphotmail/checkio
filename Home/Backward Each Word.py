#  In a given string you should reverse every word, but the words should stay in their places.
#
# Input: A string.
#
# Output: A string.
#
# Example:
#
# backward_string_by_word('') == ''
# backward_string_by_word('world') == 'dlrow'
# backward_string_by_word('hello world') == 'olleh dlrow'
# backward_string_by_word('hello   world') == 'olleh   dlrow'
#
#  Precondition: The line consists only from alphabetical symbols and spaces.
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-backward-each-word { 5 }

# Great! But how does join() manage to insert needed spase quantity? The question is about the case
# str.split(' ') will treat group of whitespaces as empty strings separated by whitespaces.
# 'hello   world'.split(' ') == ['hello', '', '', 'world']
def backward_string_by_word1(text):
    return ' '.join(word[::-1] for word in text.split(' '))

def backward_string_by_word(text: str) -> str:
    # your code here
    spaces = []

    rwords = []
    ss = ''
    rtext = ''

    if ' ' not in text:
        return text[::-1]

    words = text.split()

    for s in text:
        if s.isspace() == True :
            ss = ss + s
        else:
            if len(ss) != 0:
                spaces.append(ss)
                ss = ''

    for w in words:
        rw = w[::-1]
        rwords.append(rw)

    for i in range(0,len(rwords)):
        rtext = rtext + rwords[i]
        if i != len(rwords)-1:
            rtext = rtext + spaces[i]

    return rtext



if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")