#You are given a string and you have to find its first word.

def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    # your code here
    return text.split(' ')[0]

def first_word2(text):
    index = text.find(" ")
    return text[:index] if index != -1 else text

if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word("a word") == "a"
    assert first_word("hi") == "hi"
    print("Coding complete? Click 'Check' to earn cool rewards!")
