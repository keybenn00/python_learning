s = input()
rub = 0
kop = 0

for symb in s:
    kop += 60
    if kop >= 100:
        rub += 1
        kop -= 100

print(f'{rub} р. {kop} коп.')