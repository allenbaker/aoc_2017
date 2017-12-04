
with open("input.txt", "r") as file:
    input = file.read().replace('\n', '')

total_sum = 0

i = 0
while i < (len(input) - 2):
    if input[i] == input[i + 1]:
        total_sum += int(input[i])
    i += 1

if input[0] == input[-1]:
    total_sum += int(input[0])

print(total_sum)