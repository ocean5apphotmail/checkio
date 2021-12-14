##
# You are at the beginning of a password series. Every mission is based on the previous one. The missions that follow will become slightly more complex.

#In this mission, you need to create a password verification function.

#The verification condition is:

#    the length should be bigger than 6.

#Input: A string.

#Output: A bool.

#Example:
#is_acceptable_password('short') == False
#is_acceptable_password('muchlonger') == True
#1
#2

#How it’s used: For a password verification form. Also it’s good to learn how the task can be evaluated.
#How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-acceptable-password-1 { 18 }
#

def is_acceptable_password(password: str) -> bool:
    # your code here
    return len(password) > 6

def is_acceptable_password2(password: str) -> bool:
    return bool(password[7::])

if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")