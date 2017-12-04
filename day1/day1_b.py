
with open("input.txt", "r") as file:
    input = file.read().replace('\n', '')

total_sum = 0
half_way = int(len(input) / 2)

i = 0
while i < half_way:
    if input[i] == input[i + half_way]:
        total_sum += int(input[i])
    i += 1
print(total_sum * 2)