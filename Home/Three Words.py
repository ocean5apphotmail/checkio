#  Let's teach the Robots to distinguish words and numbers.
#
# You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession . For example, the string "start 5 one two three 7 end" contains three words in succession.
#
# Input: A string with words.
#
# Output: The answer as a boolean.
#
# Example:
#
# checkio("Hello World hello") == True
# checkio("He is 123 man") == False
# checkio("1 2 3 4") == False
# checkio("bla bla bla bla") == True
# checkio("Hi") == False
#  How it is used: This teaches you how to work with strings and introduces some useful functions.
#
# Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
# 0 < len(words) < 100
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-task-three-words { 37 }
import re

def checkio2(words):
    return True if re.search('\D+\s\D+\s\D+', words) else False

def checkio(words: str) -> bool:
    ws = words.split()
    countstr = 0
    for w in ws:
        if w.isnumeric() == True :
            countstr = 0
        else:
            countstr = countstr + 1
            if countstr == 3:
                return True
    return False


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")