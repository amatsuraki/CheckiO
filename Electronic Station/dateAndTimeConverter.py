#!/usr/bin/python
# -*- Coding: utf-8 -*-

def date_time(time: str) -> str:
    month_name = ['January', 'February' ,'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
    time = time.split(" ")
    timeA = time[0]
    timeB = time[1]

    timeA = timeA.split(".")
    day = int(timeA[0])
    mon = int(timeA[1]) - 1
    month = month_name[mon]
    year = str(int(timeA[2])) + " year"

    timeB = timeB.split(":")
    hours = int(timeB[0])
    minutes = int(timeB[1])
    if hours is 1:
        hours = str(hours) + " hour"
    else:
        hours = str(hours) + " hours"
    if minutes is 1:
        minutes = str(minutes) + " minute"
    else:
        minutes = str(minutes) + " minutes"

    time = str(day)+" "+month+" "+year+" "+hours+" "+minutes
    return time

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")