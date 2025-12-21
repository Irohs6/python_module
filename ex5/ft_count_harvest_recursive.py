
def recursive(nb: int):
    if nb > 0:
        recursive(nb - 1)
        print("Day",nb )

def ft_count_harvest_recursive():
    nb_days = int(input("Days until harvest: "))
    recursive(nb_days)
    print("Harvest time!")