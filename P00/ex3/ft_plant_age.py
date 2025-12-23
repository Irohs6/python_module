def ft_plant_age():
    age_plant = input("Enter plant age in days: ")
    if int(age_plant) > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")