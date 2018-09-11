#!/usr/bin/python
# -*- Coding: utf-8 -*-
"""
[Time converter 12h to 24h]
You are the modern man who prefers the 24-hour time format. But the 12-hour format is used in some places. Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'
"""

def time_converter(time):
    time = time.split(" ")
    time0 = time[0].split(":")
    hour = int(time0[0])
    minute = time0[1]
    
    if time[1] == "a.m.":
        if hour is not 12:
            hour = "{0:02d}".format(hour)
        else:
            hour = "00"
    else:
        if hour is not 12:
            hour = "{0:02d}".format(hour + 12)
        else:
            hour = "12"

    return str(hour + ":" + minute)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
    
"""
メモ
12:00am = 00:00
12:00pm = 12:00
if time[1] is "a.m.":   ->false
if time[1] == "a.m.":   ->true
isは同じオブジェクトではなくidが異なるためfalseになる

datetime.strptimeを使うと良い
"""