weight = float(input())
height = float(input())
IMT = weight / (height * height)

if 18.5 <= IMT <= 25:
    print('Оптимальная масса')
elif 25 < IMT:
    print('Избыточная масса')
else:
    print('Недостаточная масса')