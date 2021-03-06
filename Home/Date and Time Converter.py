#  Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
# Your task is simple - convert the input date and time from computer format into a "human" format.
#
# example
#
# Input: Date and time as a string
#
# Output: The same date and time, but in a more readable format
#
# Example:
# date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
# date_time("19.09.2999 01:59") == "19 September 2999 year 1 hour 59 minutes"
# date_time("21.10.1999 18:01") == "21 October 1999 year 18 hours 1 minute"
# # NB: words "hour" and "minute" are to be used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# # In other cases "hours" and "minutes" should be used.
#  How it is used: To improve the understanding between computers and humans.
#
# Precondition :
# 0 < day <= 31
# 0 < month <= 12
# 0 < year <= 3000
# 0 <= hours < 24
# 0 <= minutes < 60
# How to improve this mission? https://github.com/XanderVi/checkio-mission-date-time { 12 }
def date_time(time: str) -> str:
    # replace this for solution
    from datetime import date
    year = time[6:10]
    month = str(int(time[3:5]))
    day = str(int(str(time[:2])))
    hour = str(int(time[11:13]))
    min = str(int(time[14:]))

    if month == '1':
        hmonth = 'January'
    elif month == '2':
        hmonth = 'February'
    elif month == '3':
        hmonth = 'March'
    elif month == '4':
        hmonth = 'April'
    elif month == '5':
        hmonth = 'May'
    elif month == '6':
        hmonth = 'June'
    elif month == '7':
        hmonth = 'July'
    elif month == '8':
        hmonth = 'August'
    elif month == '9':
        hmonth = 'September'
    elif month == '10':
        hmonth = 'October'
    elif month == '11':
        hmonth = 'November'
    elif month == '12':
        hmonth = 'December'

    if hour == '1' and min == '1':
        time = day + ' ' + hmonth + ' ' + year + ' ' + 'year' + ' ' + hour + ' ' + 'hour' + ' ' + min + ' ' + 'minute'
    elif hour == '1' and min != '1':
        time = day + ' ' + hmonth + ' ' + year + ' ' + 'year' + ' ' + hour + ' ' + 'hour' + ' ' + min + ' ' + 'minutes'
    elif hour != '1' and min == '1':
        time = day + ' ' + hmonth + ' ' + year + ' ' + 'year' + ' ' + hour + ' ' + 'hours' + ' ' + min + ' ' + 'minute'
    else:
        time = day + ' ' + hmonth + ' ' + year + ' ' + 'year' + ' ' + hour + ' ' + 'hours' + ' ' + min + ' ' + 'minutes'

    return time


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert (
        date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
    ), "Millenium"
    assert (
        date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes"
    ), "Victory"
    assert (
        date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
    ), "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
