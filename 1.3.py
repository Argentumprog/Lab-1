numbers = [1, 2, 2, 3, 3, 3, 4, 2, 4, 4, 5, 9]

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

filtered_numbers = []
for num in numbers:
    if count_dict[num] <= 2:
        filtered_numbers.append(num)

filtered_numbers.sort(reverse=True)

print(filtered_numbers)
