str_numbers = input().split()
str_numbers = [int(el) for el in str_numbers]
count_nums_more_then_present = 0

for num in range(1, len(str_numbers)):
    if str_numbers[num] > str_numbers[num - 1]:
        count_nums_more_then_present += 1

print(count_nums_more_then_present)