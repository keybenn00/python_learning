number = input()[::-1]
number_change = ''
counter = 0

for symb in number:
    counter += 1
    if counter % 3 == 0:
        number_change += symb + ','
    else:
        number_change += symb

print(number_change[::-1].lstrip(','))