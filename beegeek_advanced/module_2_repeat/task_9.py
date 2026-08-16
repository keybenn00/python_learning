count_dots = int(input())
first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0


for _ in range(count_dots):
    dots = input().split()
    dots = [int(el) for el in dots]
    if dots[0] == 0 or dots[1] == 0:
        continue
    else:
        if dots[0] > 0:
            if dots[1] > 0:
                first_quarter += 1
            else:
                fourth_quarter += 1
        else:
            if dots[1] > 0:
                second_quarter += 1
            else:
                third_quarter += 1

print(f'Первая четверть: {first_quarter}')
print(f'Вторая четверть: {second_quarter}')
print(f'Третья четверть: {third_quarter}')
print(f'Четвертая четверть: {fourth_quarter}')