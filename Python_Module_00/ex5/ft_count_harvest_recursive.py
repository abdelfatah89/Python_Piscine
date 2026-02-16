def ft_count_harvest_recursive(i=0, days=0):
    if (not days and not i):
        days = int(input("Days until harvest: "))
        i = 1
    if (i <= days):
        print("Day", i)
        i += 1
        ft_count_harvest_recursive(i, days)
    else:
        print("Harvest time!")
