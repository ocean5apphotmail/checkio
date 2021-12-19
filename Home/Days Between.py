#  How old are you in a number of days? It's easy to calculate - just subtract your birthday from today. We could make this a real challenge though and count the difference between any dates.
#
# You are given two dates as an array with three numbers - a year, month and day. For example: 19 April 1982 will be (1982, 4, 19). You should find the difference in days between the given dates. For example between today and tomorrow = 1 day. The difference will always be either a positive number or zero, so don't forget about the absolute value.
#
# Input: Two dates as tuples of integers.
#
# Output: The difference between the dates in days as an integer.
#
# Example:
#
# days_diff((1982, 4, 19), (1982, 4, 22)) == 3
# days_diff((2014, 1, 1), (2014, 8, 27)) == 238
#  How it is used: Python has batteries included, so in this mission you’ll need to learn how to use completed modules so that you don't have to invent the bicycle all over again.
#
# Precondition: Dates between 1 january 1 and 31 december 9999. Dates are correct.
# How to improve this mission? https://github.com/CheckiO-Missions/checkio-mission-days-diff { 18 }

def days_diff(a, b):
    # your code here
    from datetime import date
    da = date(int(a[0]),int(a[1]),int(a[2]))
    db = date(int(b[0]),int(b[1]),int(b[2]))
    c = db - da

    return abs(int(c.days))


if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")