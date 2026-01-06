def ft_water_reminder():
    need_water = int(input("Days since last watering: "))
    if need_water > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
