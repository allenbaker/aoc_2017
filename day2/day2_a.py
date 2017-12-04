with open("input.txt", "r") as file:

    checksum = 0
    for line in file:
        values = [int(x) for x in line.split()]
        max_value = max(values)
        min_value = min(values)
        difference = max_value - min_value
        checksum += difference

    print(checksum)
