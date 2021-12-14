####
#Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

#Input: A string.

#Output: An iterable of strings.
###

#split_pairs('abcd') == ['ab', 'cd']
#split_pairs('abc') == ['ab', 'c_']

def split_pairs(a):

    list = []
    if len(a) == 0:
        return list

    if len(a) % 2 != 0:
        a = a + '_'

    for i in range(0, len(a)-1)[::2]:
        list.append(a[i:i+2])

    return list
    # your code here
    # reduce(lambda x, y: x * 10 + y, map(char2num, s))

### zip()

def split_pairs1(a):
    return [ch1+ch2 for ch1,ch2 in zip(a[::2],a[1::2]+'_')]

split_pairs2 = lambda a: [i + k for i, k in zip(a[::2], a[1::2] + '_')]

def split_pairs3(a):
    a += '_' if len(a) % 2 else ''
    return [a[i:i + 2] for i in range(0, len(a), 2)]

if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")

