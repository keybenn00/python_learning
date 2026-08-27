# тут нет list1 т.к в задаче программа сама подает на вход list1
cnt_num = 0
sum_num = 0

for li in list1:
    for el in li:
        cnt_num += 1
        sum_num += el

print(sum_num / cnt_num)

