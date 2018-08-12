def sun_angle(time):
    # 15°/h = 0.25°/min
    # 06:00 = 360min, 18:00 = 1080min
    time = time.split(":")
    t = int(time[0]) * 60 + int(time[1])

    if 360 <= t <= 1080:
        degree = (t - 360) * 0.25
        return degree
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
