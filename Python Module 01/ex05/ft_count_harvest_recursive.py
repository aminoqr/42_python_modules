def ft_count_harvest_recursive(day=None):
    harvest = 0
    if day is None:
        day = int(input("Days until harvest: "))
        harvest = day
    elif day == 0:
        return
    ft_count_harvest_recursive(day-1)
    print(f"Day {day}")
    if harvest == day:
        print("Harvest time!")
