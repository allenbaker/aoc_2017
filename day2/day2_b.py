with open("input.txt", "r") as file:
    check_sum = 0
    for line in file:
        values = [int(x) for x in line.split()]
        values.sort(reverse=True)
        for i, item in enumerate(values):
            for j in range(i + 1, len(values)):
                if item % values[j] == 0:
                    check_sum += (item / values[j])
    print(int(check_sum))