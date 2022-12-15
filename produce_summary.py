# "Delivered 18 Scaly Bark Watermelons for total of $72.00" is the goal
# will need a function (def)
# the problem seems to be that the melon, count, and amount variables
# are all using the same index


def melon_count(day, path):

    print("Day 1")
    the_file = open("um-deliveries-day-1.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]
    # changed the index of each variable to the corresponding word
        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


    print("Day 2")
    the_file = open("um-deliveries-day-2.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()


    print("Day 3")
    the_file = open("um-deliveries-day-3.txt")
    for line in the_file:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    the_file.close()

melon_count(1, "um-deliveries-day-1.txt")
melon_count(2, "um-deliveries-day-2.txt")
melon_count(3, "um-deliveries-day-3.txt")