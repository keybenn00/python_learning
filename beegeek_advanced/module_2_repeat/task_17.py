str_values = input()
maximum = 0
counter_reshka = 0

for el in str_values:
    if el == 'Р':
        counter_reshka += 1
        if counter_reshka > maximum:
            maximum = counter_reshka
    else:
        counter_reshka = 0

print(maximum)